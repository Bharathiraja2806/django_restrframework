from rest_framework import serializers
from .models import User as user_profile
from django.contrib.auth import get_user_model

auth_user = get_user_model()

class Useraerilaizer(serializers.ModelSerializer):

    class Meta:

        model = user_profile
        fields = '__all__'

class Registerserializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only = True,
        min_length = 8
    )

    class Meta:

        model = auth_user
        fields = ['id', 'username', 'email', 'password']

    def create(self, validate_data):

        return auth_user.objects.create_user(
            username=validate_data['username'],
            email=validate_data.get('email', ''),
            password=validate_data['password']
        )
        

class UserserilizerProfile(serializers.ModelSerializer):

    class Meta:

        model = auth_user
        fields = ["username", "email", "password"]