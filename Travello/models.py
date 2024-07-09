from django.db import models

# Create your models here.

class Destinations(models.Model):
    name =models.CharField(max_length=100)
    image=models.ImageField()
    descr=models.TextField()
    price =models.IntegerField()
    offer=models.BooleanField()
    
