from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from taggit.managers import TaggableManager
from django.conf import settings
import django.utils.timezone as timezone


# Using existing User Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=19)
    gender = models.CharField(max_length=100, choices=settings.GENDER_CHOICES, default='Unknown')
    into = models.CharField(max_length=100, choices=settings.GENDER_CHOICES, default='Unknown')
    birth = models.DateField(default=timezone.now())
    region = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, choices=settings.STATUS_CHOICES, default='Unknown')
    tags = TaggableManager(blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        output_size = (250, 250)
        img.thumbnail(output_size)
        img.save(self.image.path)




