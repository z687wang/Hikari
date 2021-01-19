from mona.models import Category, Post, Comment
from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_flex_fields import FlexFieldsModelSerializer
from .models import Image
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        expandable_fields = {
            'posts': ('mona.PostSerializer', {'many': True})
        }

class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'content', 'created', 'updated']
        expandable_fields = {
            'post': CategorySerializer,
            'user': 'mona.UserSerializer'
        }

class PostSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'title', 'content', 'created', 'updated', 'public']
        expandable_fields = {
            'category': ('mona.CategorySerializer', {'many': True}),
            'comments': ('mona.CommentSerializer', {'many': True}),
            'image': ('mona.ImageSerializer', {'many': True}),
        }

class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='post_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image', 'public']

