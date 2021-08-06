from django.contrib import admin
from .models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'active', 'working_time')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number')

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'categories', 'companies', 'active', 'order_num', 'views_count', 'value', 'terms', 'duration', 'max_coupons', 'pin', 'is_active_every_day', 'start_date', 'end_date')

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'companies', 'number')

class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')

class CompanySocialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'companies', 'socials', 'link')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'users', 'discounts', 'text')

class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'discount', 'status', 'start_time', 'deadline')

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'companies', 'cities', 'street', 'house', 'latitude', 'longitude')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(CompanySocials, CompanySocialsAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)

