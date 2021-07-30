from . import views
from django.urls import path

urlpatterns = [
    path('discount/list', views.discount_list),
    path('discount/<int:pk>', views.discount_detail),
]