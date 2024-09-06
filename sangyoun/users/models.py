from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user_id = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,  default='O')
    birth = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    short_description = models.CharField(max_length=500, null=True, blank=True)