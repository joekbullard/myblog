# blog/models.py
from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from taggit.managers import TaggableManager
from django_extensions.db.fields import AutoSlugField

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True, null=False)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title')
    post_image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = MarkdownxField()
    status = models.IntegerField(choices=STATUS, default=0)
    tags = TaggableManager()

    @property
    def formatted_markdown(self):
        return markdownify(self.body)

    @property
    def formatted_markdown_summary(self):
        return markdownify(self.body[:200] + "...")

    def word_count(self):
        return len(self.body.split(' '))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug}) # new
    
    class Meta:
        ordering = ['-created']
    
    
    
