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
    status = models.TextField(choices=STATUS_CHOICES,default='pending')




class Realestate(models.Model):
    
    STATUS_CHOICES = (
         ('pending','PENDING'),
         ('draft','DRAFT'),
         ('published','PUBLISHED'),
         ('sold','SOLD'),
         ('invoiced','INVOICED')
    )


    address = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    province = models.JSONField()
    district = models.JSONField()
    subDistrict = models.JSONField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='realestate_category'
    )

    
    status = models.TextField(choices=STATUS_CHOICES,default='pending')