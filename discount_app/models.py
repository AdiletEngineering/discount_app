from datetime import datetime
from django.db import models


class Category(models.Model):
    name = models.CharField("Название категории", max_length=50)


class Product(models.Model):
    categories = models.ForeignKey(to=Category, on_delete=models.DO_NOTHING)
    name = models.CharField("Название продукта", max_length=100)
    image = models.TextField("Ссылка на картинку продукта")
    description = models.TextField("Описание продукта")
    active = models.BooleanField(verbose_name="Продукт активен ?", default=True)
    working_time = models.CharField("Режим работы", max_length=50)


class Discount(models.Model):
    products = models.ForeignKey(to=Product, on_delete=models.DO_NOTHING)
    value = models.IntegerField("Процент скидки")
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(default=datetime(year=2999, month=12, day=31))


class Phone(models.Model):
    products = models.ForeignKey(to=Product, on_delete=models.DO_NOTHING)
    number = models.CharField("Номер телефона", max_length=10)
    type = models.CharField("Whatsapp or Telegram", max_length=20)


class Social(models.Model):
    products = models.ForeignKey(to=Product, on_delete=models.DO_NOTHING)
    name = models.CharField("Название соц сети", max_length=50)
    image = models.TextField("Ссылка на картинку социальной сети")
    link = models.TextField("Ссылка для перехода в текущую соц сеть")


class View(models.Model):
    products = models.ForeignKey(to=Product, on_delete=models.DO_NOTHING)
    count = models.IntegerField("Счетчик просмотров")


class Address(models.Model):
    products = models.ForeignKey(to=Product, on_delete=models.DO_NOTHING)
    city = models.CharField("Город", max_length=50)
    street = models.CharField("Улица", max_length=50)
    house = models.CharField("Дом", max_length=10)
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")
