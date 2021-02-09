from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import Category,Post,CategoryType



def index(request):
    
    categories = Category.objects.all()

    return render(
        request,
        'blog/index.html',
        {
            'categories':categories
        }
    )



def post_list(request):

    posts = Post.objects.all()

    return render (
        request,
        'blog/post_list.html',
        {
            'posts':posts
        }
    )

