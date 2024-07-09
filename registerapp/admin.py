from django.contrib import admin
from .models import regis1,AddVideo,JsonData
# Register your models here.

class registeradmin(admin.ModelAdmin):
    list_display=('id','FirstName','LastName','UserName','Password','Email')
    search_fields=('FirstName','LastName','UserName','Email')
    #list_filter=('FirstName','LastName')
    ordering=('id',)
    #list_per_page=20

admin.site.register(regis1,registeradmin)
admin.site.register(AddVideo)

class Jsondataadmin(admin.ModelAdmin):
    list_display=('id','fname','lname','email','gender','location','salary')
    search_fields=('fname','lname','email','location')
    ordering=('id',)
    list_per_page=20
admin.site.register(JsonData,Jsondataadmin)
