from django.urls import path, include
from .views import PostListView, PostDetailView, AboutPageView, TagPostView


# api_urlpatterns = format_suffix_patterns(api_urlpatterns)
# include both in urlpatterns e.g. path('api/locations', include(api_urlpatterns))
urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('tag/<slug:tag_slug>', TagPostView.as_view(), name='index_by_tag'),
]
