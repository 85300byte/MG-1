from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Inquiry, Testimonial
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    products = Product.objects.all()[:3]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    context = {
        'products': products,
        'testimonials': testimonials
    }
    return render(request, 'main/home.html', context)

def about(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    context = {
        'testimonials': testimonials
    }
    return render(request, 'main/about.html', context)

def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main/products.html', context)

def quality(request):
    return render(request, 'main/quality.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save inquiry to database
        inquiry = Inquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        # Send email notification
        try:
            send_mail(
                f'New Inquiry: {subject}',
                f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')

        return redirect('contact')

    return render(request, 'main/contact.html')
