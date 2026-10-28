from django.shortcuts import render
from .serializer import Useraerilaizer, Registerserializer, UserserilizerProfile
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User
from rest_framework import status
from django.contrib.auth import authenticate, get_user_model
from rest_framework.permissions import AllowAny,  IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

auth_user = get_user_model()

# Create your views here.
@api_view(['GET'])
def users(request):
    user_data = User.objects.all()
    serializer = Useraerilaizer(user_data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):

    if request.method == 'POST':
        serializer = Useraerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_fun(request, pk):

    try:
        users = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serailizer = Useraerilaizer(users)
        return Response(serailizer.data)

    elif request.method == 'PUT':
        serializer = Useraerilaizer(users, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):

    serializer = Registerserializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response({"message" : "Registeration successfull", "user" : serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({
            "error" : "username and password are required"
        },
        status=status.HTTP_400_BAD_REQUEST
        )

    user = authenticate(
        request, 
        username=username,
        password=password
    )

    if user is not None:
        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "login successfull",
            "access" : str(refresh.access_token),
            "refresh" : str(refresh),
            "username" : user.username
        }, 
        status=status.HTTP_200_OK)
    
    return Response(
        {"error": "Invalid username or password"},
        status=status.HTTP_401_UNAUTHORIZED
    )

@api_view(["GET"])
def user_profile(request):

    user_data = auth_user.objects.all().order_by('id')

    serializer = UserserilizerProfile(user_data, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
    