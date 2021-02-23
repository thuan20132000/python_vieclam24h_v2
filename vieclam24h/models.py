from django.db import models
from django.contrib.auth.models import User


# Create your models here.
 


class Image(models.Model):
     STATUS_CHOICES = (
          ('published','PUBLISHED'),
          ('draft','DRAFT')
     )

     image_url = models.TextField()
     status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='published')
     # created_at = models.DateTimeField(auto_now_add=True)
     # updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.image_url





# class User(AbstractBaseUser):
#      STATUS_CHOICES = (
#           ('pending','PENDING'),
#           ('draft','DRAFT'),
#           ('published','PUBLISHED')
#      )

#      username = models.CharField(max_length=250)
#      email  = models.EmailField(max_length=250)
#      phonenumber = models.CharField(max_length=11)
#      id_card = models.CharField(max_length=11)

#      address = models.JSONField()
#      profile_image = models.ImageField(blank=True,upload_to='upload/')
#      status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
#      created_at = models.DateTimeField(auto_now_add=True)
#      updated_at = models.DateTimeField(auto_now=True)

#      def __str__(self):
#           return self.email




class Category(models.Model):

     STATUS_CHOICES = (
         ('pending','PENDING'),
         ('draft','DRAFT'),
         ('published','PUBLISHED')

     )

     name = models.CharField(max_length=250)
     slug = models.CharField(max_length=250)
     image = models.ImageField(blank=True,upload_to='upload/')
     status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')

     def __str__(self):
          return self.name






class Occupation(models.Model):

     STATUS_CHOICES = (
         ('pending','PENDING'),
         ('draft','DRAFT'),
         ('published','PUBLISHED')
     )

     name = models.CharField(max_length=250)
     slug = models.CharField(max_length=250)
     image = models.ImageField(blank=True,upload_to='upload/')
     status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')


     category = models.ForeignKey(
          Category,
          on_delete=models.CASCADE,
          related_name='occupation'
     )

     def __str__(self):
          return self.name

     



class Job(models.Model):

     STATUS_CHOICES = (
         ('pending','PENDING'),
         ('draft','DRAFT'),
         ('published','PUBLISHED')
     )

     name = models.CharField(max_length=250,null=True)
     slug = models.CharField(max_length=250,null=True)
     image = models.ImageField(blank=True,upload_to='upload/')
     status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')

     description = models.TextField(null=True)
     suggestion_price = models.DecimalField(decimal_places=2,max_digits=18)
     location = models.JSONField()

     author = models.ForeignKey(
          User,
          on_delete=models.CASCADE,
          related_name='job_author'          
     )

     occupation = models.ForeignKey(
          Occupation,
          on_delete=models.CASCADE,
          related_name='occupation'
     )

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.name
     





class JobCollaborator(models.Model):
     STATUS_CHOICES = (
         ('confirmed','CONFIRMED'),
         ('cancel','CANCEL'),
         ('pending','PENDING')
     )

     expected_price = models.DecimalField(max_digits=18,decimal_places=2)
     descriptions = models.TextField(null=True)
     confirm_price = models.DecimalField(max_digits=18,decimal_places=2)
     start_time = models.DateTimeField(null=True)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')

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

     def __str__(self):
          return self.job




class Reivew(models.Model):
     STATUS_CHOICES = (
         ('pending','PENDING'),
         ('draft','DRAFT'),
         ('published','PUBLISHED')
     )
     review_level = models.IntegerField()
     review_content = models.TextField(null=True)
     images = models.JSONField()
     status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
     # created_at = models.DateTimeField(auto_now_add=True)
     # updated_at = models.DateTimeField(auto_now=True)

     job_collaborator = models.ForeignKey(
          JobCollaborator,
          on_delete=models.CASCADE,
          related_name='job_collaborator'
     )

     def __str__(self):
          return self.review_content





