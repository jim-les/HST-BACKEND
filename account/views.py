from django.shortcuts import render
from rest_framework_simplejwt.tokens import Token
from .models import User
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import send_otp_email, generate_otp
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Token:
        return super().get_token(user)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getroutes(request):
    routes = [
        'api/token/',
        'api/token/refresh/',
    ]
    return Response(routes)


class UserRegister(APIView):
    """
    This class registers a new User
    Attributes:
        None
    functions:
        post: registers a new user
        get: returns all the users
    
    """
    @extend_schema(
        request=UserSerializer,
        responses={201: UserSerializer}
    )
    def post(self, request):
        """
        This function registers a new user
        Args:
            param1: request
        Returns:
            response: returns a response object
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

    @extend_schema(
        responses= UserSerializer(many=True)
    )
    def get(self, request):
        """
        This function returns all the users
        Args:
            param1: request
        Returns:
            response: returns a response object
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

@extend_schema(
    responses= UserSerializer(many=True)
)
class UserVerification(APIView):
    """
    This class verifies a user
    Attributes:
        None
    functions:
        post: send email to the user with otp
        get: verifies the otp and returns a token
    """
    serializer_class = UserSerializer

    @extend_schema(responses=UserSerializer(many=True))
    def post(self, request, userid, otp):
        """
        This function verifies the otp sent 
        Args:
            param1: request
            param2: userid
            param3: otp
        Returns:
            response: returns a response object
        """
        user = User.objects.get(id=userid)
        if user.otp == otp:
            user.is_verified = True
            user.save()
            return Response({'message': 'User verified successfully'}, status.HTTP_200_OK)
        return Response({'message': 'Invalid OTP'}, status.HTTP_400_BAD_REQUEST)
    

    @extend_schema(responses= UserSerializer(many=True))
    def get(self, request, userid):
        """
        This function generates an otp upon a get request and then sends it via email to the user
        Args:
            param1: request
            param2: userid
        Returns:
            response: returns a response object
        """
        user = User.objects.get(id=userid)
        otp = generate_otp()
        user.otp = otp
        user.save()
        send_otp_email(user.email, otp)
        return Response({'message': 'OTP sent successfully'}, status.HTTP_200_OK)
        