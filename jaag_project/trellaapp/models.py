from django.db import models

# Create your models here.

class data(models.Model):
    name=models.CharField(max_length=20,default="")
    age=models.IntegerField(default="")
    address=models.CharField(max_length=50,default="")
    contact=models.IntegerField(default="")
    mail=models.CharField(max_length=50,default="")
