from django.urls import path, include
from .views import *

# api urlpattern
api_urlpatterns = [
    path('api/post/', UserList.as_view()),
    path('api/post/<int:pk>/', UserDetail.as_view())
]

# include both in urlpatterns e.g. path('api/locations', include(api_urlpatterns))
urlpatterns = [
    path('<slug:slug>', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('api/', include(api_urlpatterns)),
    path('', IndexPageView.as_view(), name='index'),
]