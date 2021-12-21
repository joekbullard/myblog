from django.urls import path, include
import rest_framework
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

# api urlpattern
api_urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

api_urlpatterns = format_suffix_patterns(api_urlpatterns)

# include both in urlpatterns e.g. path('api/locations', include(api_urlpatterns))
urlpatterns = [
    path('<slug:slug>', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('api/', include(api_urlpatterns)),
    path('', IndexPageView.as_view(), name='index'),
]