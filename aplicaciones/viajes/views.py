from django.shortcuts import render

# Create your views here.

def viajes_url(request):
    return render(request ,'viajes/viajes.html',{})