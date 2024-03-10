from django.shortcuts import render
from .models import *

# Create your views here.

def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'base/Store.html', context)

def cart(request):
	context = {}
	return render(request, 'base/Cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'base/Checkout.html', context)