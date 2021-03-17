from django.contrib import admin
from .models import Category,CategoryType,Post,Comment
# Register your models here.


admin.site.register(Category)




admin.site.register(CategoryType)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('email','content','post','created_at','updated_at')
    list_filter = ('status','created_at','updated_at')
    search_fields = ('email','content')