from rest_framework import serializers
from .models import Users
from .validators import validate_password


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Users
        fields = ('old_password', 'password', 'password2')


class LoginViewSerializer(serializers.ModelSerializer):
    pass