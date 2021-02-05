from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('publisged','Published')
    )
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')


    class Meta:
        ordering = ('-publish',)




