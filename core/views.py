from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from blog.models import BlogPost
from .models import ContactMessage
from .forms import ContactForm


def home(request):
    """Home page view"""
    # Get latest 3 blog posts for preview
    latest_posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')[:3]
    
    context = {
        'latest_posts': latest_posts,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About Us page view"""
    return render(request, 'core/about.html')


def services(request):
    """Services page view"""
    services_data = [
        {
            'icon': 'fas fa-pills',
            'title': 'Importation of Pharmaceutical Products',
            'description': 'We import high-quality pharmaceutical products from reputable manufacturers worldwide, ensuring compliance with international standards.',
            'features': ['Quality Assurance', 'Regulatory Compliance', 'Global Sourcing']
        },
        {
            'icon': 'fas fa-medkit',
            'title': 'Supply of Medical Equipment',
            'description': 'Comprehensive medical equipment supply for hospitals, clinics, and healthcare facilities with cutting-edge technology.',
            'features': ['Modern Equipment', 'Technical Support', 'Training Available']
        },
        {
            'icon': 'fas fa-truck',
            'title': 'Distribution & Logistics',
            'description': 'Efficient and reliable distribution network ensuring timely delivery of medical supplies across the region.',
            'features': ['Cold Chain Logistics', 'Real-time Tracking', 'Emergency Delivery']
        },
        {
            'icon': 'fas fa-shield-alt',
            'title': 'Regulatory Compliance Support',
            'description': 'Expert guidance on regulatory requirements and compliance for pharmaceutical products and medical devices.',
            'features': ['Documentation Support', 'Regulatory Updates', 'Compliance Training']
        }
    ]
    
    context = {
        'services': services_data,
    }
    return render(request, 'core/services.html', context)


def contact(request):
    """Contact Us page view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)


# Product Views
from .models import Product
from django.shortcuts import get_object_or_404
from django.contrib import messages


def products(request):
    """View for displaying all products"""
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'core/products.html', context)


def product_detail(request, pk):
    """View for displaying single product details"""
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'core/product_detail.html', context)
