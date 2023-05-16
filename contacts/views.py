from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


def inquiry(request):
    if request.method == "POST":
        data = {
            'car_id': request.POST['car_id'],
            'car_title': request.POST['car_title'],
            'user_id': request.POST['user_id'],
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'customer_need': request.POST['customer_need'],
            'city': request.POST['city'],
            'state': request.POST['state'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'message': request.POST['message']
        }
        if request.user.is_authenticated:
            has_contact = Contact.objects.filter(car_id=data['car_id'], user_id=data['user_id'])
            if has_contact:
                messages.error(request, "The inquiry is submitted already")
                return redirect('/cars/' + data['car_id'])
            admin_info = User.objects.get(is_superuser=True)
            admin_email = admin_info.email
            contact = Contact(**data)
            contact.save()
            send_mail(
                subject=f'Inquiry for {data["car_title"]}',
                message=f"You have the new inquiry for the {data['car_title']}. Login to admin pannel for more detail about inquiry",
                from_email=data['email'],
                recipient_list=[admin_email],
                fail_silently=False
            )

            messages.success(request, "Your request has been submitted, we will get back to you shortly")
            return redirect('/cars/' + data['car_id'])
