from rest_framework import serializers


class AddressSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    street_name = serializers.CharField(max_length=50 , trim_whitespace=True)
    city_name = serializers.CharField(max_length=20,trim_whitespace=True)
    state_name = serializers.CharField(max_length=20,trim_whitespace=True)
    country_name = serializers.CharField(max_length=20,trim_whitespace=True)
    zipcode = serializers.CharField(max_length=10,trim_whitespace=True )

class UpdateAddressSerializer(serializers.Serializer):
    street_name = serializers.CharField(max_length=50, trim_whitespace=True)
    city_name =serializers.CharField(max_length=20, trim_whitespace=True)
    state_name = serializers.CharField(max_length=20, trim_whitespace=True)
    country_name = serializers.CharField(max_length=20, trim_whitespace=True)
    zipcode = serializers.CharField(max_length=10, trim_whitespace=True)