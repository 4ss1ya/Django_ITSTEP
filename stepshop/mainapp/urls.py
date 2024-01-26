from django.contrib import admin
from django.urls import path

from .views import index,products,contacts,about,product

app_name = 'main'

urlpatterns = [
    path('index/', index),
    path('products/', products),
    path('contacts/', contacts),
    path('about/', about),
    path('product/', product),
]
