# blog/models.py
from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=250)
    post_image = models.ImageField(default='default.png', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField(null=False)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
    
    
    
