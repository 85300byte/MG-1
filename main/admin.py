from django.contrib import admin
from .models import Product, Inquiry, Testimonial

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'curcumin_content', 'is_organic', 'created_at')
    list_filter = ('is_organic', 'created_at')
    search_fields = ('name', 'description')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'rating', 'created_at', 'is_active')
    list_filter = ('rating', 'is_active', 'created_at')
    search_fields = ('name', 'company', 'content')
