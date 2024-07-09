from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class regis1(models.Model):
    FirstName=models.TextField(max_length=200)
    LastName=models.TextField(max_length=200)
    UserName=models.TextField(max_length=200)
    Password=models.CharField(max_length=100)
    Email=models.EmailField()

class AddVideo(models.Model):
    video = EmbedVideoField()

class JsonData(models.Model):
    fname=models.TextField(max_length=100) 
    lname=models.TextField(max_length=100) 
    email=models.EmailField() 
    gender=models.TextField(max_length=100)  
    location=models.TextField(max_length=100)  
    salary=models.IntegerField()