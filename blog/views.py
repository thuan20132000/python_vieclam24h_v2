from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

from .models import Category,Post,CategoryType,Comment
from taggit.models import Tag
from .forms import Post,CommentForm,SearchForm

from django.contrib.postgres.search import SearchVector


def index(request):
    
    categories = Category.objects.all()
    posts = Post.objects.filter(status='published').order_by('-id')


    return render(
        request,
        'blog/index.html',
        {
            'categories':categories,
            'posts':posts
        }
    )



def post_list(request,tag_slug=None,category_type_slug=None):

    posts = Post.objects.filter(status='published')

    tags = None
    if tag_slug:
        tags = get_object_or_404(
            Tag,
            slug=tag_slug
        )
        posts = posts.filter(tags__in=[tags])

    if category_type_slug:
        category_types = get_object_or_404(
            CategoryType,
            slug=category_type_slug
        )
        posts = posts.filter(category_type=category_types)


    paginator = Paginator(posts,10)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)
    
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    return render (
        request,
        'blog/post_list.html',
        {
            'posts':posts,
            'page':page
        }
    )




def post_detail(request,post):

    post = get_object_or_404(
        Post,
        slug=post
    )
    post.views = post.views + 1
    post.save()

    tags = post.tags.all()

    comments = post.blog_comment.filter(status='published')


    if request.method == 'POST':
        comment = Comment()
        # A comment was posted
        email = request.POST['email']
        content = request.POST['content']

        if email and content:
            comment.email = email
            comment.content = content
            comment.post = post
            comment.save()
        
            email = ''
            content = ''

   

    return render(
        request,
        'blog/post_detail.html',
        {
            'post':post,
            'tags':tags,
            'comments':comments
        }
    )




def post_search(request):
    form = SearchForm()
    query =None
    results = []


    searchs = request.POST

    # print(search_value['search_value'])

    if searchs['search_value']:
        results = Post.objects.filter(status='published').annotate(
                search=SearchVector('title','content'),
            ).filter(search=searchs['search_value'])

    
    return render(
        request,
        'blog/search.html',
        {
            'form':form,
            'query':query,
            'results':results
        }
    )