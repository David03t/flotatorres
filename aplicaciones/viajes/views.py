from django.shortcuts import render, redirect
from .models import Viajes, Ciudades , Horario , Tarifas, Vehiculos, Usuarios
from.forms import ViajesForm

# Create your views here.

def viajes_url(request):
    viajes = Viajes.objects.all()
    viaje = {'viajes': viajes}
    return render(request ,'viajes/viajes.html', viaje)

def insertar_viajes(request):
    Ciudad = Ciudades.objects.all()
    Hora = Horario.objects.all()
    Tarifa = Tarifas.objects.all()
    Vehiculo = Vehiculos.objects.all()
    Usuario = Usuarios.objects.raw('SELECT * from usuarios where tipo_de_persona = 2;')
    if(request.method == 'GET'):
        forms = ViajesForm()
        tipos = { 'Ciudad': Ciudad,'Hora': Hora ,'Tarifa': Tarifa ,'Vehiculo': Vehiculo ,'Usuario': Usuario , 'form': forms}
    else:
        forms = ViajesForm(request.POST)   
        tipos = {  'Ciudad': Ciudad,'Hora': Hora ,'Tarifa': Tarifa ,'Vehiculo': Vehiculo ,'Usuario': Usuario , 'form': forms }
        if forms.is_valid():
            forms.save()
            return redirect('viajes_url')
    return render(request, 'viajes/add_viajes.html',tipos )
    
def actualizar_viajes(request,id):
    Ciudad = Ciudades.objects.all()
    Hora = Horario.objects.all()
    Tarifa = Tarifas.objects.all()
    Vehiculo = Vehiculos.objects.all()
    Usuario = Usuarios.objects.raw('SELECT * from usuarios where tipo_de_persona = 2;')
    viajes = Viajes.objects.get(id=id)
    if(request.method == 'GET'):
        forms = ViajesForm(instance= viajes)
        tipos = { 'Ciudad': Ciudad,'Hora': Hora ,'Tarifa': Tarifa ,'Vehiculo': Vehiculo ,'Usuario': Usuario , 'form': forms}
    else:
        forms = ViajesForm(request.POST, instance= viajes)   
        tipos = {  'Ciudad': Ciudad,'Hora': Hora ,'Tarifa': Tarifa ,'Vehiculo': Vehiculo ,'Usuario': Usuario , 'form': forms }
        if forms.is_valid():
            forms.save()
            return redirect('viajes_url')
    return render(request, 'viajes/Update_viajes.html',tipos )

def borrar_viajes(request,id):
    viajes = Viajes.objects.get(id = id)
    viajes.delete()
    return redirect('viajes_url')