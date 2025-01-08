from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="The Axon Journal")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    cover_image = CloudinaryField('cover_image', null=True, blank=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')