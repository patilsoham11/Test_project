from django.db import models

# Create your models here.


class User_info(models.Model):
    username= models.CharField(max_length=200)
    Email= models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=12)
    address1 = models.CharField("Address line 1",max_length=1024,)
    massege = models.CharField(max_length=1024,)
    created = models.DateTimeField(auto_now_add=True)
    agree =models.BooleanField()