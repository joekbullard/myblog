from django.urls import path
from .views import IndexPageView, AboutPageView, BlogDetailView

urlpatterns = [
    path('<slug:slug>', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', IndexPageView.as_view(), name='index'),
]