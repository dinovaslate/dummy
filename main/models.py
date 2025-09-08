from django.db import models
import uuid

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=30)
    is_featured = models.BooleanField()

# Create your models here.
