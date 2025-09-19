from django.db import models
# Create your models here.

# class Patient(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField(null=True, blank=True)
#     disease = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class login(models.Model):
    username =models.CharField(max_length=100)
    password=models.IntegerField(null=True,blank=True)
    user=models.CharField(max_length=100)