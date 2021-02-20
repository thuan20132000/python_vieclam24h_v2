from django import template
from ..models import Post,Category
from django.db.models import Count


register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.filter(status='published').count()



@register.simple_tag
def get_most_commented_posts(count=3):
    return Post.objects.filter(status='published').annotate(
        total_comments=Count('blog_comment')
    ).order_by('-total_comments')[:count]



@register.inclusion_tag('blog/layout/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('created_at')[:count]

    return {
        'latest_posts':latest_posts
    }




@register.inclusion_tag('blog/layout/navbar.html')
def show_navbar():
    category = Category.objects.all()

    return {
        'category':category
    }



# @register.inclusion_tag('blog/layout/searchbar.html')
# def show_searchbar():
    

#     return {

#     }
