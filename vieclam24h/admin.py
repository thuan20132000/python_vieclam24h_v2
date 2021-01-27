from django.contrib import admin

from .models import Category,Occupation
# Register your models here.



class AdminCategory(Category):
    pass

admin.site.register(Category)



class AdminOccupation(Occupation):
    pass

admin.site.register(Occupation)