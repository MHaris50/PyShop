from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Offer


def home(request):
    offers = Offer.objects.all()
    featured_products = Product.objects.all()[:3]
    return render(request, 'home.html', {
        'offers': offers,
        'featured_products': featured_products
    })


def index(request):
    products = Product.objects.all()
    offers = Offer.objects.all()
    return render(request, 'index.html', {
        'products': products,
        'offers': offers
    })


def new(request):
    return HttpResponse("New products")

