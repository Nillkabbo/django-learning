from django.shortcuts import render
from store.models import Product


def say_hello(request):
    all_products = Product.objects.all()
    return render(request, 'hello.html', {'name': all_products})
