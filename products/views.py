from django.shortcuts import render
from .models import Product 

# Create your views here.

def products(request):
    """ View to show products """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)