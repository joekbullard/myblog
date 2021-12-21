from rest_framework import generics, permissions
from . import serializers
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.models import User
from .models import Post
from .permissions import IsOwnerOrReadOnly

class IndexPageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'all_posts_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


# API Views
# View names should be in the following form: 
# {ModelName}List and {ModelName}Detail for a list of objects and a single object, respectively.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer