from django.db import models

# # Create your models here.
# //// name of table would be Emplyee 
#
class Login(models.Model):
    name=models.CharField(Max_length=30)
    email=models.EmailField(Max_length=40)
    password=models.CharField(Max_length=40)
    