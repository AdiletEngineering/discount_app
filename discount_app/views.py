from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .dtos import *
from .serializers import *



@api_view(['GET', 'POST'])
def discount_list(request):
    if request.method == 'GET':
        discounts = Discount.objects.all()
        dto_object = toDiscountDto(discounts)
        serializer = DiscountDtoSerializer(dto_object, many=True)
        return Response(serializer.data)
    


#
@api_view(['GET', 'POST'])
def discount_detail(request, pk):
    if request.method == 'GET':
        discount = Discount.objects.get(pk=pk)
        serializer = DiscountSerializer(discount)
        return Response(serializer.data)



