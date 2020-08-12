from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profil_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save() #saves the original form along with whatever else

        img = Image.open(self.image.path)

        if img.height > 70 or img.width > 70:
            output_size = (70,70)
            img.thumbnail(output_size)
            img.save(self.image.path)
