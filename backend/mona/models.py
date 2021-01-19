from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    class_id = models.IntegerField(unique=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ManyToManyField('mona.Image', related_name='posts')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    public = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, related_name='posts')
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='liked_post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='liker', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} : {}'.format(self.user, self.post)

class Comment(models.Model):
    content = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.content

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi',
    )
    image_ppoi = PPOIField()
    public = models.BooleanField(default=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name
