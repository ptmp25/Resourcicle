from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    photos = models.ManyToManyField('Photo')

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')