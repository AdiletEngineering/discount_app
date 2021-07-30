from django.contrib import admin
from .models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'active', 'working_time')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number')

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'categories', 'companies', 'views_count', 'value', 'terms', 'is_active_every_day', 'start_date', 'end_date')

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'companies', 'number', 'type')

class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'companies', 'name', 'image', 'link')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'users', 'discounts', 'text')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'companies', 'city', 'street', 'house', 'latitude', 'longitude')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Address, AddressAdmin)

