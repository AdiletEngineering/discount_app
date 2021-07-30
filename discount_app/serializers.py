from rest_framework import serializers
from .models import *
from .dtos import *

# сериалайзер для class DiscountDto
class DiscountDtoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    image = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=50)
    value = serializers.IntegerField()
    views_count = serializers.IntegerField()



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    categories = CategorySerializer()
    companies = CompanySerializer()
    class Meta:
        model = Discount
        fields = '__all__'




