from os import name
from django.contrib import admin
from django.urls import path
from tienda_virtual import views

urlpatterns = [
    path('', views.Home, name = 'Home'),
    path('servicios', views.Servicios, name = 'Servicios'),
    path('tienda', views.Tienda, name = 'Tienda'),
    path('blog', views.Blog, name = 'Blog'),
    path('contacto', views.Contacto, name = 'Contacto'),
]