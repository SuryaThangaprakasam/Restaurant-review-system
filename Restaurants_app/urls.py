from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('restaurants/', views.restaurant_list,name='restaurant_list'),
    path('restaurant/<int:pk>', views.restaurant_detail,name='restaurant_detail'),
]