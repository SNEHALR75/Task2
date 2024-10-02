from django.urls import path
from .api import *


urlpatterns = [
    path('add/',create_product),
    path('show/',show_product),
    path('retrieve/<pk>/',retrieve_product),
    path('update/<pk>/',update_product),
    path('delete/<pk>/',delete_product),
    
]