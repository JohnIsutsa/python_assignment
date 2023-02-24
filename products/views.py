import django
from django.shortcuts import render
from django.http import HttpResponseRedirect
from products.models import *
from products.forms import *
from django.core import serializers
from django.http import JsonResponse



# Create your views here.
def get_all_products(request):
    # get all products in the database
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def get_a_product(request, product_id):
    product = None
    try:
        product = Product.objects.get(id = product_id)
        
    except Product.DoesNotExist:
        product = None
    
    return render(request, 'product.html', {'product': product})

def get_all_products_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    print(json_data)
    return JsonResponse({"results": json_data})

# def add_product(request):
#     if request.method == 'POST':
#         product_form = ProductForm(request.POST)
#         if forms.is_valid():
#             csrf_token = django.middleware.csrf.get_token(request)