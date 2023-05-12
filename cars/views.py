from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator


def cars(request):
    cars = Car.objects.order_by("-created_date")
    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        "cars": paged_cars,
    }
    return render(request, 'cars/cars.html', data)


def car_details(request, id):
    car = get_object_or_404(Car, pk=id)
    data = {
        "car": car,
    }
    return render(request, 'cars/car_details.html', data)
