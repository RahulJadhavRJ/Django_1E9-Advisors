from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinations
# Create your views here.

def index(request):
    obj1 = Destinations()
    obj1.name='Mumbai'
    obj1.descr='Mumbai, one of the major cosmopolitan cities in India'
    obj1.price=4500
    obj1.image='destination_4.jpg'
    obj1.offer=False

    obj2 = Destinations()
    obj2.name='Latur'
    obj2.descr='Anybody can fit here within a days'
    obj2.price=900
    obj2.image='dest11.jpg'
    obj2.offer=True

    obj3 = Destinations()
    obj3.name='Pune'
    obj3.descr='one of the largest IT hubs in India'
    obj3.price=2900
    obj3.image='dest12.jpg'
    obj3.offer=False
    
    obj=[obj1, obj2, obj3]

    return render(request,'index.html',{'obj':obj})