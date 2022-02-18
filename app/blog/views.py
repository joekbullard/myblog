from .models import Post, Comment
from taggit.models import Tag
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


class PostListView(ListView):
    paginate_by = 10
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.filter(status=1)
    context_object_name = 'posts'


class TagPostView(ListView):
    template_name = 'filtered.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status=1).filter(tags__slug__in=[self.kwargs.get('tag_slug')])

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(TagPostView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['tag_name'] = Post.objects.filter(status=1).filter(tags__slug=self.kwargs.get('tag_slug')).values('title', 'tags__name')[0]['tags__name']
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
