from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import Category,Product

def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(status='published')
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    
    return render(request,
                'ecommerce/product/list.html',
                {
                    'category':category,
                    'categories':categories,
                    'products':products
                })





def product_detail(request,id,slug):
    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        status='published'
    )

    return render(
        request,
        'ecommerce/product/detail.html',
        {'product':product}
    )