from rest_framework import serializers
# import user model from contrid.auth
from django.contrib.auth.models import User
from .models import Post
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

# inherit from ModelSerializer class
class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'posts']


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'owner',
            'body',
            'created', 
            'updated', 
            'status',
            'tags'
            ]

