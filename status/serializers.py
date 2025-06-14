from rest_framework import serializers
from .models import Status
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        fields = ('id', 'username', 'email')

       
class StatusSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Status
        fields = ('id', 'text', 'image_link', 'created_at', 'user', 'is_active', 'is_private')
        read_only_fields = ('created_at', 'user')