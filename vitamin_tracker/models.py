from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Vitamin(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='blog_pics')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title


