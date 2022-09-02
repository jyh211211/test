from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pic=models.ImageField(upload_to='user/%y/%m')    
    def __str__(self):
        return self.username

    def getpic(self):
        if self.pic:
            return self.pic.url
        return '/media/No_image.png'