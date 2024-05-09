from rest_framework import serializers
from user import models

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = models.CustomUser
        fields = '__all__'