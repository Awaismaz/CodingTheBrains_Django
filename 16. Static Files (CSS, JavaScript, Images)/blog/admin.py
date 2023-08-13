from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    list_filter = ('created_date', 'published_date', 'author')
    search_fields = ('title', 'text')
    date_hierarchy = 'published_date'
    ordering = ['-published_date', 'author']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date', 'text')
    list_filter = ('created_date', 'author')
    search_fields = ('author', 'text')
    date_hierarchy = 'created_date'
    ordering = ['-created_date', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
