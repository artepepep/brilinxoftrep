from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20)
    company_name = serializers.CharField(max_length=205)
    interested_service = serializers.CharField(max_length=100)
    details = serializers.CharField()