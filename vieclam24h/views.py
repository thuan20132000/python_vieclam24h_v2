from django.shortcuts import render

# Create your views here.

from .models import Category,Job
from .serializers import CategorySerializer,JobSerializer

# rest
from rest_framework  import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def category_list_api(request):
    # List all category
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)




@api_view(['GET'])
def job_list_api(request):
    if request.method == 'GET':
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs,many=True)
        
        return Response(serializer.data)

