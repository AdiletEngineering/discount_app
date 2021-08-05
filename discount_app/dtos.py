from .models import *

class DiscountListDto:
    def __init__(self, discount):
        self.id = discount.id
        self.name = discount.companies.name
        self.image = discount.companies.image
        self.description = discount.companies.description
        self.city = Address.objects.filter(companies=discount.companies.id).first().cities.name
        self.value = discount.value
        self.views_count = discount.views_count

def toDiscountListDto(discounts):
    list = []
    for discount in discounts:
        discount_dto = DiscountListDto(discount)
        list.append(discount_dto)
    return list


class DiscountDetailDto:
    def __init__(self, discount):
        self.id = discount.id
        self.views_count = discount.views_count
        self.value = discount.value
        self.terms = discount.terms
        self.is_active_every_day = discount.is_active_every_day
        self.name = discount.companies.name
        self.image = discount.companies.image
        self.description = discount.companies.description
        self.working_time = discount.companies.working_time
        self.address = Address.objects.filter(companies=discount.companies.id)
        self.socials = Social.objects.filter(companies=discount.companies.id)
        self.reviews = discount.reviews

def toDiscountDetailDto(discount):
    discount_dto = DiscountDetailDto(discount)
    return discount_dto