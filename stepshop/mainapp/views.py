from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def product(request):
    return render(request, 'product.html')
