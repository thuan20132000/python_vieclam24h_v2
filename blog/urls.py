
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('',views.index,name='blog'),
    path('post-list/<slug:category_type_slug>/',views.post_list,name='post_list_by_category_type'),
    path('post-list/',views.post_list,name='post_list'),
    path('post-detail/<slug:post>',views.post_detail,name='post_detail'),
    path('tag/<slug:tag_slug>/',views.post_list,name='post_list_by_tag'),
    path('feed/',LatestPostsFeed(),name='post_feed'),
    path('search/',views.post_search,name='post_search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
   