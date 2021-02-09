from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

from taggit.managers import TaggableManager

from django_quill.fields import QuillField


class Category(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
        ('pending','Pending'),
    )

    title = models.CharField(max_length=150)
    metaTitle = models.CharField(max_length=250,null=True)
    image = models.ImageField(blank=True,upload_to='upload/blog/')
    slug = models.SlugField(max_length=150)
    content = models.TextField(null=True)
    status = models.TextField(max_length=10,choices=STATUS_CHOICES,default='published')


    def __str__(self):
        return f" - {self.title}"



class CategoryType(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
        ('pending','Pending'),
    )

    title = models.CharField(max_length=150)
    metaTitle = models.CharField(max_length=250,null=True)
    slug = models.SlugField(max_length=250)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.TextField(max_length=10,choices=STATUS_CHOICES,default='published')

    category = models.ForeignKey(
        Category,
        related_name='post_category_type_category',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id}- {self.title}"


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
        ('pending','Pending'),
    )


    title = models.CharField(max_length=250)
    metaTitle = models.CharField(max_length=250,null=True)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    image = models.ImageField(blank=True,upload_to='upload/blog/')
    summary = models.TextField()
    content = QuillField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')

    tags = TaggableManager()

    category_type = models.ForeignKey(
        CategoryType,
        related_name='blog_post_category_type',
        on_delete=models.CASCADE
    )
    

    def __str__(self):
        return f"{self.id} - {self.title}"







class Comment(models.Model):
    STATUS_CHOICES = (
        ('published','Published'),
        ('hidden','hidden')
    )
    
    title = models.CharField(max_length=150)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=STATUS_CHOICES,default='published')

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='blog_comment'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_comment_author'
    )


    def __str__(self):
        return f"{self.id} - {self.title}"