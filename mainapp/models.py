from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *
class CustomUser(AbstractUser):
    username = None
    phone_number = models.IntegerField(unique=True)
    email = models.EmailField(null=True,blank=True)
    user_bio = models.CharField(max_length=50,null=True,blank=True)
    user_profile_image = models.ImageField(upload_to="profile")
    # Ham yaha pe aor field ko add kar sakte hai
 
    USERNAME_FIELD = 'phone_number' # username ki jagah pe ab phone_number ka use hoga hame yaha pe jis field se login karana chahte hai usko yaha pe add karenge
    REQUIRED_FIELDS = []
    objects = UserManager()
# model ko 2 type se customize kar sakte hai
    #1.abstract user class
    #2.abstract base user class