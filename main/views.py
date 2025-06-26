from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Inquiry, Testimonial
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import logging

# Set up logging
logger = logging.getLogger(__name__)

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

        # Prepare email content
        email_subject = f'New Contact Form Submission: {subject}'
        
        # Create HTML email content
        html_message = render_to_string('main/email/contact_notification.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message,
        })

        # Send email notification to admin
        try:
            # Send notification to admin
            admin_email = EmailMessage(
                subject=email_subject,
                body=html_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.ADMIN_EMAIL],  # List of admin email addresses
                reply_to=[email],  # This allows direct reply to the customer
            )
            admin_email.content_subtype = "html"  # Main content is now text/html
            admin_email.send(fail_silently=False)
            
            # Send confirmation email to customer
            customer_subject = "Thank you for contacting Golden Spice Venture"
            customer_html = render_to_string('main/email/contact_confirmation.html', {
                'name': name,
            })
            
            # Send confirmation to customer
            customer_email = EmailMessage(
                subject=customer_subject,
                body=customer_html,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],  # Customer's email address
            )
            customer_email.content_subtype = "html"
            customer_email.send(fail_silently=False)
            
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            logger.info(f"Contact form submission successful from {email}")
            
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later or contact us directly via phone.')
            logger.error(f"Email sending error: {str(e)}", exc_info=True)

        return redirect('main:contact')

    return render(request, 'main/contact.html')
