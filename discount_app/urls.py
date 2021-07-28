from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.product_list),
]