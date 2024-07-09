from django.urls import path

from registerapp import views

urlpatterns=[
    path('',views.registerpage,name='registerpage'),
    path('showdata/',views.showdata,name='showdata'),
    path('video/',views.showVideo,name='showVideo'),
    path('jsondata/',views.jsondataadd,name='jsondataadd')
]