from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.





class Category(models.Model):

    STATUS_CHOICE = (
        ("pending","Pending"),
        ("draft","Draft"),
        ("published",'Published')
    )

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords",max_length=255,help_text="Comma-delimited set of SEO keywords  for meta tag")
    meta_description = models.CharField("Meta Description",max_length=255,help_text="Content for description meta tag")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=STATUS_CHOICE,default="pending")


    class Meta:
        ordering  = ['name']
        verbose_name_plural = 'Categories'
        verbose_name = 'category'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('ecommerce:product_list_by_category',args=[self.slug])

    


class Product(models.Model):
    STATUS_CHOICE = (
        ("pending","Pending"),
        ("draft","Draft"),
        ("published",'Published')
    )

    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=255,unique=True,help_text='Unique value for product page URL, create from name')
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,default=0.00)
    image = models.ImageField(upload_to='upload/ecommerce')
    is_active = models.BooleanField(default=True)
    is_bestller = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField("Meta Keywords",max_length=255,help_text="Comma-delimited set of SEO keywords  for meta tag")
    meta_description = models.CharField("Meta Description",max_length=255,help_text="Content for description meta tag")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=STATUS_CHOICE,default="pending")

    categories = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']
        index_together = (('id','slug'))

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('ecommerce:product_detail',args=[self.id,self.slug])
