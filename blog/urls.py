from django.urls import path
from .views import IndexPageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', IndexPageView.as_view(), name='index'),
]