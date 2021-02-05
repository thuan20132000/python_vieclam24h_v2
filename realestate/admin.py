from django.contrib import admin

# Register your models here.

from .models import Category,Realestate


class AdminRealestateCategory(admin.ModelAdmin):
    list_display = ('name','slug','status','image')


admin.site.register(Category,AdminRealestateCategory)



admin.site.register(Realestate)