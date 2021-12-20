# blog/models.py
from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=False, unique=True, max_length=250)
    post_image = models.ImageField(default='default.png', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = MarkdownxField()
    status = models.IntegerField(choices=STATUS, default=0)

    @property
    def formatted_markdown(self):
        return markdownify(self.body)

    def formatted_markdown_summary(self):
        return markdownify(self.body[:200] + "...")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug}) # new
    
    class Meta:
        ordering = ['-created']
    
    
    
