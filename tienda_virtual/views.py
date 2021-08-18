
from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.


def Home(request):
    return render (request, 'tienda_virtual/home.html')


def Servicios(request):
    return render (request, 'tienda_virtual/servicios.html')


def Tienda(request):
    return render (request, 'tienda_virtual/tienda.html')

def Blog(request):
    return render (request, 'tienda_virtual/blog.html')

def Contacto(request):
    return render (request, 'tienda_virtual/contacto.html')
