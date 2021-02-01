from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 

class Category(models.Model):

    STATUS_CHOICES = (
         ('pending','PENDING'),
         ('draft','DRAFT'),
         ('published','PUBLISHED')

    )

    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    image = models.ImageField(blank=True,upload_to='upload/')
    status = models.TextField(choices=STATUS_CHOICES,default='pending')





class Occupation(models.Model):

     STATUS_CHOICES = (
         ('pending','PENDING'),
         ('draft','DRAFT'),
         ('published','PUBLISHED')
     )

     name = models.CharField(max_length=250)
     slug = models.CharField(max_length=250)
     image = models.ImageField(blank=True,upload_to='upload/')
     status = models.IntegerField(choices=STATUS_CHOICES)

     category = models.ForeignKey(
          Category,
          on_delete=models.CASCADE,
          related_name='occupation'
     )
     



class Job(models.Model):

     STATUS_CHOICES = (
         ('pending','PENDING'),
         ('draft','DRAFT'),
         ('published','PUBLISHED')
     )

     name = models.CharField(max_length=250)
     slug = models.CharField(max_length=250)
     image = models.ImageField(blank=True,upload_to='upload/')
     status = models.IntegerField(choices=STATUS_CHOICES)

     occupation = models.ForeignKey(
          Occupation,
          on_delete=models.CASCADE,
          related_name='occupation'
     )
     




class JobCollaborator(models.Model):
     STATUS_CHOICES = (
         ('pending','PENDING'),
         ('draft','DRAFT'),
         ('published','PUBLISHED')
     )

     expected_price = models.DecimalField(max_digits=18,decimal_places=2)
     descriptions = models.TextField(null=True)
     confirm_price = models.DecimalField(max_digits=18,decimal_places=2)
     review_content = models.TextField(null=True)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     job = models.ForeignKey(
          Job,
          on_delete=models.CASCADE,
          related_name='job_collaborators',
     )

     collaborator = models.ForeignKey(
          User,
          on_delete=models.CASCADE,
          related_name='collaborator'

     )
