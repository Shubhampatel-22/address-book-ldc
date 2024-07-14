from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import AddressSerializer,UpdateAddressSerializer
from ..utils.helpers import generate_uuid_v4 , write_data_to_json_file,read_data_from_json_file,\
    search_from_json,find_address_in_json,is_address_id_exist,update_json_file,delete_data_from_json


class AddAddressApiView(APIView):
    def post(self,resquest):
        try:
            serializer = AddressSerializer(data=resquest.data)

            if not serializer.is_valid():
                return Response({
                    "message": f"{serializer.errors}",
                    "success": False
                }, status=400)
            address_data = serializer.validated_data
            
            is_address_exist = find_address_in_json("address.json", address_data)

            if is_address_exist:
                return Response({
                    "data":None,
                    "message":"This address already exists in address book.",
                }, status=200)
            
            address_data['_id'] = generate_uuid_v4()
            write_data_to_json_file('address.json',address_data)

            return Response({
                "data":address_data,
                "message":"Address added successfully"
            },status=201)
        
        except Exception as error:
            return Response({
                "data":{},
                "message":f"{str(error)}"
            }, status=500)
        

class GetAddressApiView(APIView):
        def get(self, request):
            try:
                if 'search' in request.GET:
                    # print(request.GET.get('q'))
                    query_result = search_from_json(request.GET.get('search'))
                    # print(query_result)
                    if len(query_result)==0:
                        return Response({
                            "data":None,
                            "message":"No result found"
                        } ,status=200)
                    return Response({
                        "data":query_result ,
                        "message": f"address data from query",
                        "success": True
                    }, status=200)
                
                all_address_data = read_data_from_json_file('address.json')
                return Response({
                        "data":all_address_data,
                        "message": f"all address data",
                        "success": True
                    }, status=200)
            except Exception as error:
                return Response({
                        "data":None,
                        "message": f"{str(error)}",
                        "success": False
                    }, status=500)
            
class UpdateAddressApiView(APIView):
    def put(self, request):
        try:
            if 'id' not in request.GET:
                return Response({
                    "data":None,
                    "message": f"ID is required to update the data",
                    "success": False
                }, status=400)
            
            _id = request.GET['id']
            is_valid_id = is_address_id_exist("address.json", _id)
            if not is_valid_id:
                return Response({
                    "data":None,
                    "message": f"Invalid Id.",
                    "success": False
                }, status=400)
            
            serializer = UpdateAddressSerializer(data=request.data)

            if not serializer.is_valid():
                return Response({
                    "data":None,
                    "message": f"{serializer.errors}",
                    "success": False
                }, status=400)
            address_data = serializer.validated_data
            is_address_exist = find_address_in_json("address.json", address_data)

            if is_address_exist:
                return Response({
                    "data":is_address_exist,
                    "message":"This data already exists in address book.",
                    "success": True
                }, 200)
                
            
            updated_address = update_json_file("address.json", _id, address_data)
            
            return Response({
                "data": updated_address,
                "message":"Address updated successfully in addressbook.",
                "success": True
            }, 201)

        except Exception as error:
            return Response({
                    "data":None,
                    "message": f"{str(error)}",
                    "success": False
                }, status=500)


class DeleteAddressApiView(APIView):
    def delete(self, request):
            try:
                if 'id' not in request.GET:
                    return Response({
                        "data":None,
                        "message": f"ID is required to delete the data",
                        "success": False
                    }, status=400)
                
                _id = request.GET['id']
                is_valid_id = is_address_id_exist("address.json", _id)
                if not is_valid_id:
                    return Response({
                        "data":None,
                        "message": f"Invalid Id.",
                        "success": False
                    }, status=400)
                delete_data_from_json("address.json", _id)
                return Response({
                    "data":{},
                    "message": "Address deleted successfully.",
                    "success":True
                })
            except Exception as error:
                return Response({
                    "data": None,
                    "message":f"{str(error)}",
                    "success":False   
                }, 500)