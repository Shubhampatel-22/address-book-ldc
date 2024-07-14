import json
import re
from uuid import uuid4 as v4

def generate_uuid_v4():
    return str(v4())


def read_data_from_json_file(file_path):
    try:
        database = open(file_path)
        content = json.load(database)
        return content

    except json.JSONDecodeError as error:
        return Exception(f"Unable to read {file_path} file:  {str(error)}")


def write_data_to_json_file(file_path, data):
    try:
        content = read_data_from_json_file(file_path)
        database = open(file_path, 'w')
        content[data['_id']] = data        
        content = json.dumps(content)
        database.write(content)

        return content
        
    except Exception as error:
        print("write_file_exception", error)
        return Exception(f"Unable to write in {file_path} file: {str(error)}")
    

def find_address_in_json(file_path, address):
    try:
    # Open the JSON file and load its content
        with open(file_path, 'r') as f:
            all_address_data = json.load(f)

            current_address = address["street_name"]+address["city_name"]+address["state_name"]+ \
                                address["country_name"]+address["zipcode"]
            
            current_address=current_address.lower()
            
            for _,value in all_address_data.items():
                existing_address = value["street_name"]+value["city_name"]+value["state_name"]+ \
                                value["country_name"]+value["zipcode"]
                existing_address = existing_address.lower()
                if current_address == existing_address:
                    return value
            return None
            # lowercase_address = {k.lower(): v.lower() for k, v in address.items()}
            # for _, value in all_address_data.items():
            #     existing_address ={k.lower(): v.lower() for k, v in value.items()} 
            #     existing_address.pop('_id')
            #     if lowercase_address == existing_address:
            #         return value
                
            # # Address not found
            # return None

    except (FileNotFoundError, json.JSONDecodeError) as e:
    # Handle potential errors: file not found or invalid JSON format
        print(f"Error: {e}")
        return None
    

def update_json_file(file_path, _id, data):
    try:
        content = read_data_from_json_file(file_path)
        user_to_update = content[_id]

        for key, value in data.items():
                user_to_update[key] = value

        write_data_to_json_file(file_path, user_to_update)
        return user_to_update
    
    except Exception as error:
        print("update_file_exception", error)
        return Exception(f"Unable to update {file_path} file: {str(error)}")
    

def delete_data_from_json(file_path, _id):
    try:
        content = read_data_from_json_file(file_path)
        content.pop(_id)
        
        write_data_to_json_file(file_path, content)
        return True
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return None
    

def is_address_id_exist(file_path,_id):
    data = read_data_from_json_file(file_path)
    for _, value in data.items():
        if value['_id'] == _id:
            return True
    return False


def search_from_json(query):
    data = read_data_from_json_file('address.json')
    results = {}
    # print(query)
    pattern = re.compile(query, re.IGNORECASE)  # Compile regex pattern, ignoring case
    # print(pattern.search('ashok'))
    for _id, entry in data.items():
        if (pattern.search(entry["username"]) or
            pattern.search(entry["street_name"]) or
            pattern.search(entry["city_name"]) or
            pattern.search(entry["state_name"]) or
            pattern.search(entry["country_name"]) or
            pattern.search(entry["zipcode"])):
            results[_id] = entry
    # print(results)
    return results

# def is_valid_zipcode(zipcode):
#     # Regular expression for a basic validation
#     # This pattern allows for 3-10 alphanumeric characters with optional spaces and dashes
#     pattern = r'^[a-zA-Z0-9\s\-]{3,10}$'

#     print("hello")
    
#     # Compile the regex pattern
#     regex = re.compile(pattern)
#     print(bool(regex.match(zipcode.strip())))
#     # if not regex.match(zipcode.strip()):
#     # Check if the zipcode matches the pattern
#     return bool(regex.match(zipcode.strip()))
    
