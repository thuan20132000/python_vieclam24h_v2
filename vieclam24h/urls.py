
from django.urls import path
from . import views



app_name = 'vieclam24h'




urlpatterns = [
    path('api/v1/category-list',views.category_list_api,name='category_list_api'),
    path('api/v1/job-list',views.job_list_api,name='job_list_api'),
    

]