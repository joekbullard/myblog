from django.contrib import admin
from .models import Post, Comment
from markdownx.admin import MarkdownxModelAdmin


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'created',)
    inlines = [
        CommentInLine
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
