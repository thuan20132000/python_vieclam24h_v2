from django.contrib import admin

# Register your models here.

from .models import Category,Realestate


class AdminRealestateCategory(Category):
    pass

admin.site.register(Category)



admin.site.register(Realestate)