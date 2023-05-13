from django.shortcuts import render
from .models import Team
from cars.models import Car


def home(request):
    teams = Team.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by("-created_date")
    city_search = Car.objects.values('city').distinct()
    year_search = Car.objects.values('year').distinct()
    model_search = Car.objects.values('model').distinct()
    body_style_search = Car.objects.values('body_style').distinct()

    data = {
        "teams": teams,
        'featured_car': featured_car,
        'all_cars': all_cars,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'model_search': model_search,
    }
    return render(request, "pages/home.html", data)


def about(request):
    teams = Team.objects.all()
    data = {
        "teams": teams
    }
    return render(request, "pages/about.html", data)


def services(request):
    return render(request, "pages/services.html")


def contact(request):
    return render(request, "pages/contact.html")
