from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    serializes the user object
    """
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id', 'created_at', 'updated_at', 'is_verified', 'otp', 'refresh_token']
        