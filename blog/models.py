from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="The Axon Journal")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    cover_image = CloudinaryField('cover_image', null=True, blank=True)
    category = models.CharField(max_length=255, default="uncategorised")
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)


    @property
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    

    def get_absolute_url(self):
        return reverse('home')