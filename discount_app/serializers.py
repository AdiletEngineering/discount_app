from rest_framework import serializers
from .models import *
from .dtos import *


class ReviewSer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class AddressSer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class SocialSer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"


# сериалайзер для class DiscountDto
class DiscountListDtoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    image = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=100)
    city = AddressSer(many=True)
    value = serializers.IntegerField()
    views_count = serializers.IntegerField()


class DiscountDetailDtoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    views_count = serializers.IntegerField()
    value = serializers.IntegerField()
    terms = serializers.CharField(max_length=500)
    name = serializers.CharField(max_length=50)
    image = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=100)
    working_time = serializers.CharField(max_length=50)
    address = AddressSer(many=True)
    socials = SocialSer(many=True)
    reviews = ReviewSer(many=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



