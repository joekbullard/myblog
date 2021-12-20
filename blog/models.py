# blog/models.py
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=250)
    post_image = models.ImageField(default='default.png', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = MarkdownxField()
    status = models.IntegerField(choices=STATUS, default=0)

    @property
    def formatted_markdown(self):
        return markdownify(self.body)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
    
    
    
