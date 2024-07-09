from django.shortcuts import render,redirect
import json
from django.contrib.auth.models import User,auth
from .models import regis1,AddVideo,JsonData
# Create your views here.

def registerpage(request):
    if request.method=='POST':
        data=request.POST
        FirstName=data.get('FirstName')
        LastName=data.get('LastName')
        UserName=data.get('UserName')
        Password=data.get('Password')
        Email=data.get('Email')
        regis1.objects.create(
            FirstName=FirstName,
            Email=Email,
            LastName=LastName,
            UserName=UserName,
            Password=Password)
        print('user created....')
        return redirect('/')
    else:
        return render(request,'registerpage.html')
    
def showdata(request):
    obj=regis1.objects.all()
    return render(request,'showdata.html',{'obj':obj})

def showVideo(request):
    viobj=AddVideo.objects.all()
    return render(request,'video.html',{'viobj':viobj})

def jsondataadd(request,*args, **kwargs):
    with open(r'C:\Users\Dell\project1\registerapp\json_data.json') as file:
        data=json.load(file)
        for item in data:
            JsonData.objects.create(
                fname=item['fname'],
                lname=item['lname'],
                email=item['email'],
                gender=item['gender'],
                location=item['location'],
                salary=item['salary']
            )
    jsonobj=JsonData.objects.all()
    return render(request,'jsondata.html',{'jsonobj':jsonobj})