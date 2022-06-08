from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio_urls(request):
    return render(request ,'inicio/index.html',{})

def bioseguridad(request):
    return render(request , 'base/bioseguridad.html',{})

def decreto(request):
    return render(request , 'base/decreto_1168.html',{})

def servicio_cliente(request):
    return render(request , 'base/servicio_al_cliente.html',{})

# def inicio(request):
#     return HttpResponse('<h1>Mi primera pagina </h1>')