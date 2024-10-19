from django.db import models

# Create your models here.
class Data(models.Model):
    Username=models.CharField(max_length=20,default="")
    Password=models.IntegerField(max_length=10,default="")