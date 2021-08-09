from django.contrib.sites import requests
from django.utils import timezone

from discount_app.models import Coupon


def my_scheduled_job():
    coupons = Coupon.objects.all()
    print('*'*200)
    for coupon in coupons:
        if coupon.deadline < timezone.now:
            coupon.status = "EXPIRED"

def do_not_sleep():
    r = requests.get('https://discount-adilet.herokuapp.com/')