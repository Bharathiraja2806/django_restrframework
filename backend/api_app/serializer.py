from rest_framework import serializers
from .models import User as user
from django.contrib.auth.models import User

class Useraerilaizer(serializers.ModelSerializer):

    class Meta:

        model = user
        fields = '__all__'

class Registerserializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only = True,
        min_length = 8
    )

    class Meta:

        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validate_data):

        user = User.objects.create_user(
            username=validate_data['username'],
            email=validate_data['email'],
            password=validate_data['password']
        )

        return user
