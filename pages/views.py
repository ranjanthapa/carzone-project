from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages


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
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        email_subject = 'You have a new message from carzone website regarding ' + subject
        message_body = f'Name:{name} Email: {email} Phone: {phone} Message:{message}'
        send_mail(
            subject=email_subject,
            message=message_body,
            from_email=email,
            recipient_list=[admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting, we will get back shortly')
        return redirect('contact')
    return render(request, "pages/contact.html")
