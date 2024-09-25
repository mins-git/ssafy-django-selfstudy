from django.shortcuts import render, redirect
from .models import Restaurants
# Create your views here.

def index(request):
    restaurants = Restaurants.objects.all()
    context = {
        'restaurants' : restaurants,
    }
    return render(request, 'restaurants/index.html', context)

def new(request):
    return render(request, 'restaurants/new.html')


def create(request):
    restaurant_name = request.POST.get('name')
    restaurant_address = request.POST.get('address')
    restaurant_description = request.POST.get('description')
    restaurant_phone_number = request.POST.get('phone_number')
    
    restaurant = Restaurants(name = restaurant_name, description = restaurant_description, address = restaurant_address, phone_number = restaurant_phone_number)
    restaurant.save()
    
    return redirect('restaurants:index')