from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class TermAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'categories', 'terms', 'name', 'image', 'description', 'active', 'working_time')

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'products', 'value', 'start_date', 'end_date')

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'products', 'number', 'type')

class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'products', 'name', 'image', 'link')

class ViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'products', 'count')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'products', 'city', 'street', 'house', 'latitude', 'longitude')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(View, ViewAdmin)
admin.site.register(Address, AddressAdmin)

