from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "username",
            "email",
            "gender",
            "country",
            "phone",
            "profile_photo",
            "password",
        ]


class LoginSerializer(Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs["username"], password=attrs["password"])
        if user is None:
            print(f"Failed login attempt for username: {attrs['username']}")
            raise serializers.ValidationError("Invalid username or password")
        attrs["user"] = user
        return attrs
