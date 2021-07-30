from .models import *

class DiscountDto:
    def __init__(self, discount):
        self.id = discount.id
        self.name = discount.companies.name
        self.image = discount.companies.image
        self.description = discount.companies.description
        self.city = Address.objects.filter(companies=discount.companies.id)[0].city
        self.value = discount.value
        self.views_count = discount.views_count

def toDiscountDto(discounts):
    list = []
    for discount in discounts:
        discount_dto = DiscountDto(discount)
        list.append(discount_dto)
    return list

