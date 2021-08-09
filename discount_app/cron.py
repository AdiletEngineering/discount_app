from django.utils import timezone

from discount_app.models import Coupon


def my_scheduled_job():
    coupons = Coupon.objects.all()
    for coupon in coupons:
        if coupon.deadline < timezone.now:
            coupon.status = "EXPIRED"