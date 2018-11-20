from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=False)
    image = models.ImageField(default='default.png', blank=True)