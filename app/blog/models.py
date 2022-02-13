# blog/models.py
from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from taggit.managers import TaggableManager
from django_extensions.db.fields import AutoSlugField
from datetime import date

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

    def formatted_date(self):
        return self.created.date().strftime('%d %b %y')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug}) # new
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = "posts"
    

class Comment(models.Model):
    post = models.ForeignKey(
        'Post', 
        on_delete=models.CASCADE, 
        related_name='comments',
        )
    user = models.CharField(null=False, max_length=30)
    comment_text = MarkdownxField()
    created = models.DateTimeField(auto_now_add=True)
    

    @property
    def formatted_markdown(self):
        return markdownify(self.comment_text)

    def __str__(self):
        return self.comment_text

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "comments"

    def get_absolute_url(self):
        return reverse('index')

