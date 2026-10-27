from django.shortcuts import render
from .serializer import Useraerilaizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from rest_framework import status

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