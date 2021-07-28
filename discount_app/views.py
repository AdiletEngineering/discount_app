from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from .models import *


@api_view(['get', 'post'])
def product_list(request):
    if request.method == 'get':
        products = Product.objects.all()
        serializer =


