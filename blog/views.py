from django.views.generic import TemplateView, ListView
from .models import Post

class IndexPageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'all_posts_list'

class AboutPageView(TemplateView):
    template_name = 'about.html'