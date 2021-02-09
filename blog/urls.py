
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'ecommerce'

urlpatterns = [
    path('',views.index,name='blog'),
    path('post-list',views.post_list,name='post_list')
 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )