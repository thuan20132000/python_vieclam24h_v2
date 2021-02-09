from django.test import TestCase

# Create your tests here.
from .models import Category,Product




class CategoryTest(TestCase):

    def setUp(self):

        for i in range(10):
            self.category = Category.objects.create(
                name=f"name {i}",
                description=f"description {i}",
                is_active=True,
                meta_keywords=f"Me ta keyworlds",
                meta_description=f"Meta description",
                
            )

