from django.contrib import admin
from .models import Category,CategoryType,Post
# Register your models here.


admin.site.register(Category)




admin.site.register(CategoryType)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass