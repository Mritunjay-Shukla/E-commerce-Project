from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    pic = models.ImageField(upload_to="account/", blank=True)
    bio = models.TextField(blank=True)
    
    REQUIRED_FIELDS = ('email',)
 
    def __str__(self): 
        return self.username

#@receiver(post_save,sender = User)
#def create_profile(sender, instance, created, **kwargs):
 #    print(sender, kwargs)
  #   if created:
   #     Profile.objects.create(user= instance)