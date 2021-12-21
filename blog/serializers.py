from rest_framework import serializers
# import user model from contrid.auth
from django.contrib.auth.models import User
from .models import Post

# inherit from ModelSerializer class
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

        

