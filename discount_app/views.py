from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .dtos import *
from .serializers import *



@api_view(['GET', 'POST'])
def discount_list(request):
    if request.method == 'GET':

        is_order_by_publish = request.query_params.get('order_by_publish')
        category = request.query_params.getlist('category')

        discounts = Discount.objects.filter(active=True)
        if is_order_by_publish == "true":
            discounts = discounts.order_by('-start_date')
        if category:
            discounts = discounts.filter(categories__id__in=category)

        dto_object = toDiscountListDto(discounts)
        serializer = DiscountListDtoSerializer(dto_object, many=True)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
def discount_detail(request, pk):
    if request.method == 'GET':
        discount = Discount.objects.get(pk=pk)
        dto_obj = toDiscountDetailDto(discount)
        serializer = DiscountDetailDtoSerializer(dto_obj)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
def review_create(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        new_review = request.data
        serializer = ReviewSer(data = new_review)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

