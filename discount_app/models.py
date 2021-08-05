from datetime import datetime
from django.db import models


class Category(models.Model):
    name = models.CharField("Название категории", max_length=50)

    def __str__(self):
        return self.name



class Company(models.Model):
    name = models.CharField("Название компании", max_length=100)
    image = models.TextField("Ссылка на картинку компании")
    description = models.TextField("Описание компании")
    active = models.BooleanField(verbose_name="Компания активна?", default=True)
    working_time = models.CharField("Режим работы", max_length=50)

    def __str__(self):
        return self.name



class User(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Discount(models.Model):
    categories = models.ForeignKey(to=Category, on_delete=models.DO_NOTHING, related_name='discounts')
    companies = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, related_name='discounts')
    active = models.BooleanField("Скидка активна?", default=True)
    views_count = models.IntegerField("Количество просмотров")
    value = models.IntegerField("Процент скидки")
    terms= models.TextField("Условия скидки")
    duration = models.DurationField("Длительность скидки")
    max_coupons = models.IntegerField("максимальное количество купонов")
    pin = models.CharField("Пин код для активации", max_length=4)
    is_active_every_day = models.TextField("акция действует каждый день?")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.terms



class Phone(models.Model):
    companies = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, related_name='phones')
    number = models.CharField("Номер телефона", max_length=20)

    def __str__(self):
        return self.number



class Social(models.Model):
    name = models.CharField("Название соц сети", max_length=50)
    image = models.TextField("Ссылка на картинку социальной сети")

    def __str__(self):
        return self.name



class CompanySocials(models.Model):
    companies = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, related_name='company_socials')
    socials = models.ForeignKey(to=Social, on_delete=models.DO_NOTHING, related_name='company_socials')
    link = models.TextField("Ссылка для перехода в текущую соц сеть")



class Review(models.Model):
    users = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name='reviews')
    discounts = models.ForeignKey(to=Discount, on_delete=models.DO_NOTHING, related_name='reviews')
    text = models.TextField("Текст отзыва")

    def __str__(self):
        return self.text



class Coupon(models.Model):
    users = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name='coupons')
    discounts = models.ForeignKey(to=Discount, on_delete=models.DO_NOTHING, related_name='coupons')
    status = models.CharField("Статус купона", max_length=50)
    start_time = models.DateField(auto_now_add=True)
    deadline = models.DateField()



class City(models.Model):
    name = models.CharField("Название города", max_length=200)

    def __str__(self):
        return self.name



class Address(models.Model):
    companies = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, related_name='addresses')
    cities = models.ForeignKey(to=City, on_delete=models.DO_NOTHING, related_name='addresses')
    street = models.CharField("Улица", max_length=100)
    house = models.CharField("Дом", max_length=10)
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")

    def __str__(self):
        return self.street
