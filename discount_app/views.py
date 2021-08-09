from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from itertools import chain
from .models import *
from .dtos import *
from .serializers import *



@api_view(['GET', 'POST'])
def discount_list(request):
    if request.method == 'GET':
        city = request.query_params.get('city')
        is_order_by_publish = request.query_params.get('order_by_publish')
        category = request.query_params.getlist('category')

        discounts = Discount.objects.filter(active=True)

        if is_order_by_publish == "true":
            discounts = discounts.order_by('-start_date')
        if category:
            discounts = discounts.filter(categories__id__in=category)
        if city:
            discounts_searched = discounts.filter(companies__addresses__cities__id=city).distinct('companies_id')
            discounts_excluded = discounts.exclude(companies__addresses__cities__id=city)
            discounts = chain(discounts_searched, discounts_excluded)

        dto_object = toDiscountListDto(discounts)
        serializer = DiscountListDtoSerializer(dto_object, many=True)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
def discount_detail(request, pk):
    if request.method == 'GET':
        discount = Discount.objects.get(pk=pk)
        dto_obj = toDiscountDetailDto(discount)
        serializer = DiscountDetailDtoSerializer(dto_obj)
        discount.views_count += 1
        discount.save()
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



@api_view(['GET', 'POST'])
def coupon_create(request):
    if request.method == 'GET':
        coupons = Coupon.objects.all()
        serializer = CouponSer(coupons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            coupon = Coupon.objects.get(user=request.data['user'], discount=request.data['discount'], status="RESERVED")
            serializers = CouponSer(coupon)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except:
            serializer = CouponSer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['PUT'])
def coupon_activate(request, id):
    if request.method == 'PUT':
        coupon = Coupon.objects.get(id=id)
        system_pin = coupon.discount.pin
        pin = request.data.get('pin')
        if system_pin == pin:
            coupon.status = 'ACTIVATED'
            coupon.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

