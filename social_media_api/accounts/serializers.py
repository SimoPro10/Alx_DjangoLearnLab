from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True)
    following = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['id', 'followers']
        fields = ['id', 'username', 'followers', 'following']




       
       