from django.db import models

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
    status = models.IntegerField(choices=STATUS_CHOICES)





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
     