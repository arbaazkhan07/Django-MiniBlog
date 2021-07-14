from django.contrib import admin
from django.urls.conf import include
from .models import Post

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']


