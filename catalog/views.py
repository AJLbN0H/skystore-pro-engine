from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')



def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context=context)


def home_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home_page.html', context=context)

