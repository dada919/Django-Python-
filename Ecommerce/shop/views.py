from django.shortcuts import render
from shop.models import Product

def index(request):
    products = Product.objects.all()

    return render(request, '../templates/index.html', context={"products": products})