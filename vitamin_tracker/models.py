from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Vitamin(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=255, null=True)
    image = models.ImageField(default='default.jpg', upload_to='blog_pics')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vitamin-detail', kwargs={'pk': self.pk})



    def save(self):
        super().save() #saves the original form along with whatever else


