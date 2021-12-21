from rest_framework import serializers
# import user model from contrid.auth
from django.contrib.auth.models import User
from .models import Post
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

# inherit from ModelSerializer class
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()
    
    class Meta:
        model = Post
        fields = [
            'title', 
            'created', 
            'updated', 
            'status',
            'tags'
            ]

