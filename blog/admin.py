from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin

class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'created',)
    prepopulated_fields = {'slug': ('title',)} # new

admin.site.register(Post, PostAdmin)