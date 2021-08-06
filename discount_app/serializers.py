from rest_framework import serializers
from .models import *
from .dtos import *

class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ReviewSer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class AddressSer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('street', 'house', 'latitude', 'longitude')

class SocialSer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('name', 'image')


class CompanySocialsSer(serializers.ModelSerializer):
    socials = SocialSer()
    class Meta:
        model = CompanySocials
        exclude = ('id', 'companies')



# сериалайзер для class DiscountDto
class DiscountListDtoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    image = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=200)
    value = serializers.IntegerField()
    views_count = serializers.IntegerField()


class DiscountDetailDtoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    views_count = serializers.IntegerField()
    value = serializers.IntegerField()
    terms = serializers.CharField(max_length=500)
    is_active_every_day = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=50)
    image = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=100)
    working_time = serializers.CharField(max_length=50)
    address = AddressSer(many=True)
    socials = CompanySocialsSer(many=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DiscountSer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class CouponSer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = ('user', 'discount')


    def create(self, validated_data):
        user = validated_data['user']
        discount = validated_data['discount']

        start_time = datetime.now()

        deadline = discount.duration + start_time

        coupon = Coupon.objects.create(user=user,
                                       discount=discount,
                                       deadline=deadline,
                                       start_time=start_time)

        return coupon


