from django.contrib import admin
from .constants import application_name
from .models import Image, Category, Comment, Like, Post

admin.site.site_header = application_name + " Admin"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'class_id', 'name', 'content')
    list_filter = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'content', 'created', 'updated')
    list_filter = ('author',)

admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Like)