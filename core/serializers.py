from rest_framework import serializers
from .models import UserDetail

class UserDetailsSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = UserDetail
        fields = ['id', 'username', 'is_active', 'reported']
    