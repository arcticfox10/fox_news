from re import U
from django.db import models


from django.contrib.auth.models import User

class UserInformation(models.Model):
    profile = models.OneToOneField(User ,primary_key=True , on_delete=models.CASCADE)
    bio = models.CharField(max_length=250)
    profile_image = models .ImageField(upload_to ='profile_images/' ,  null = True , blank=True) 