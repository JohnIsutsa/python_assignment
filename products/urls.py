from django.urls import path
from .views import *

 

urlpatterns = [
    path('get_all', get_all_products),
    path('<int:product_id>/', get_a_product),
    path('json_products/', get_all_products_json)
]