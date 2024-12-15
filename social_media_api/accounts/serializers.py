from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password

User = get_user_model().objects.create_user

class UserSerializer(serializers.ModelSerializer):
   password = serializers.CharField(write_only=True, validators=[validate_password])
   serializers.CharField() 
   class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

def create(self, validated_data):
        user = Token.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user




       
       