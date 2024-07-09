from django.urls import path

from Travello import views
urlpatterns = [
    path('',views.index,name='index')
]