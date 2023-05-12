from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.
class User(AbstractUser):
    def get_profile_image_upload_path(instance, filename):
        return os.path.join('profile_images', instance.username, filename)
    phone_number = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to=get_profile_image_upload_path, null=True, blank=True)