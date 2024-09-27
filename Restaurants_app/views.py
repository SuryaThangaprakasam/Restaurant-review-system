from django.shortcuts import render,get_object_or_404
from .models import Restaurant, Menu, Reservation, Review, User

def index(request):
    return render(request, 'base.html')

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants':restaurants})

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    reviews = restaurant.reviews.all()
    reservations = restaurant.reservations.all()
    return render(request, 'restaurant_detail.html',{'restaurant': restaurant,'reviews':reviews,'reservations':reservations})

