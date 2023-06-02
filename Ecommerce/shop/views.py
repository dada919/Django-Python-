from django.shortcuts import render
from shop.models import Product

def index(request):
    products = Product.objects.all()
    print(products.name)
    print("coucou")

    return render(request, 'index.html', context={"products": products})