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
    
    def create(self, validated_data):
        """
        this function takse the data from the request and hash the password
        arquments:
            validated_data: data from the request
        return:
            user object
        """

        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance