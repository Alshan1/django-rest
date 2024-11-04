# users/serializers.py
from rest_framework import serializers
from .models import UserData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['email', 'password', 'name']  
        extra_kwargs = {
            'password': {'write_only': True}  
        }

    def create(self, validated_data):
        user = UserData(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])  
        user.save()
        return user
