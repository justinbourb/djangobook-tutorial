from django.contrib import admin
from .models import Post
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    search_fields = ('title', 'text')
    #how to add author to search? icontains error?


admin.site.register(Post, PostsAdmin)
