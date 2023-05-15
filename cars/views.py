from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator


def cars(request):
    cars = Car.objects.order_by("-created_date")
    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    city_search = Car.objects.values('city').distinct()
    year_search = Car.objects.values('year').distinct()
    model_search = Car.objects.values('model').distinct()
    body_style_search = Car.objects.values('body_style').distinct()
    data = {
        "cars": paged_cars,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'model_search': model_search,

    }
    return render(request, 'cars/cars.html', data)


def car_details(request, id):
    car = get_object_or_404(Car, pk=id)
    data = {
        "car": car,
    }
    return render(request, 'cars/car_details.html', data)


def search(request):
    cars = Car.objects.order_by("-created_date")
    city_search = Car.objects.values('city').distinct()
    year_search = Car.objects.values('year').distinct()
    model_search = Car.objects.values('model').distinct()
    body_style_search = Car.objects.values('body_style').distinct()
    transmission_search = Car.objects.values('transmission').distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.order_by('-created_date').filter(description__icontains=keyword)

    if 'year' in request.GET:
        year = request.GET['year']
        cars = cars.order_by('-created_date').filter(year__iexact=year)

    if 'model' in request.GET:
        model = request.GET['model']
        cars = cars.order_by('-created_date').filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        cars = cars.order_by('-created_date').filter(city__iexact=city)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        cars = cars.order_by('-created_date').filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        cars = cars.order_by('-created_date').filter(body_style__iexact=transmission)

    if 'min_price' and 'max_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.order_by('-created_date').filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'model_search': model_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/search.html', data)
