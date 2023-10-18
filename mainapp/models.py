from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import *


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=13,unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to="profile")
 
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
        
    #abstract user class
    #abstract base user class