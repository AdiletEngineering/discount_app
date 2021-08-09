from apscheduler.schedulers.blocking import BlockingScheduler
from django.contrib.sites import requests
from django.utils import timezone

from discount_app.models import Coupon

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    coupons = Coupon.objects.all()
    print('*' * 200)
    for coupon in coupons:
        if coupon.deadline < timezone.now:
            coupon.status = "EXPIRED"

@sched.scheduled_job('interval', minutes=25)
def timed_job():
    r = requests.get('https://discount-adilet.herokuapp.com/')

sched.start()
