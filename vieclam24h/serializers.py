from rest_framework import serializers
from .models import Category,Job



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name','slug','image','status',)
        model = Category





class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'name',
            'slug',
            'image',
            'description',
            'suggestion_price',
            'location',
            'author',
            'occupation',
            'created_at',
            'updated_at',
            'status'
        )
        model = Job