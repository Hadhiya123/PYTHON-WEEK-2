from django.db import models

# Create your models here.

class login(models.Model):
    username =models.CharField(max_length=100)
    password=models.IntegerField(null=True,blank=True)
    user=models.CharField(max_length=100)