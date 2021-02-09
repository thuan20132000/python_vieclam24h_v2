from django.contrib import admin

# Register your models here.
from .models import Product,Category

@admin.register(Category)
class CaregoryAdmin(admin.ModelAdmin):
    list_display  = ['name','slug','status']
    list_editable = ['status']
    prepopulated_fields = {'slug':('name',)}




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','created_at','updated_at','status']
    list_filter = ['created_at','updated_at']
    list_editable = ['price','status']
    prepopulated_fields = {'slug':('name',)}