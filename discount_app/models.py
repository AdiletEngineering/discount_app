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
    active = models.BooleanField(verbose_name="Продукт активен ?", default=True)
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
    companies = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, related_name='discounts1')
    views_count = models.IntegerField("Количество просмотров")
    value = models.IntegerField("Процент скидки")
    terms= models.TextField("Условия скидки")
    is_active_every_day = models.TextField("акция действует каждый день?")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.companies



class Phone(models.Model):
    companies = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, related_name='phones')
    number = models.CharField("Номер телефона", max_length=10)
    type = models.CharField("Whatsapp or Telegram", max_length=20)

    def __str__(self):
        return self.number



class Social(models.Model):
    companies = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, related_name='socials')
    name = models.CharField("Название соц сети", max_length=50)
    image = models.TextField("Ссылка на картинку социальной сети")
    link = models.TextField("Ссылка для перехода в текущую соц сеть")

    def __str__(self):
        return self.name



class Review(models.Model):
    users = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name='reviews')
    discounts = models.ForeignKey(to=Discount, on_delete=models.DO_NOTHING, related_name='reviews1')
    text = models.TextField("Текст отзыва")



class Address(models.Model):
    companies = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, related_name='addresses')
    city = models.CharField("Город", max_length=50)
    street = models.CharField("Улица", max_length=50)
    house = models.CharField("Дом", max_length=10)
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")


