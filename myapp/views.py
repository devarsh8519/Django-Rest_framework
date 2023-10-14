from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from myapp.serializers import productserializers
from .models import product
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class=productserializers
    permission_classes=[permissions.IsAuthenticated]
    
