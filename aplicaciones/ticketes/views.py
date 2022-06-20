from django.shortcuts import render, redirect
from .models import Tickets, Usuarios, Vehiculos, Viajes
from .form import TicketsForm

# Create your views here.

def tickets_url(request):
    tickets = Tickets.objects.all()
    ticket = {'tickets':tickets}
    return render(request, 'tickets/tickets.html', ticket ) 

def insertar_ticket(request):
    Viaje = Viajes.objects.all()
    Usuario = Usuarios.objects.raw('SELECT * from usuarios where tipo_de_persona = 1;')
    if(request.method == 'GET'):
        forms = TicketsForm()
        tipos = {'Viaje':Viaje,'Usuario': Usuario , 'form': forms}
    else:
        forms = TicketsForm(request.POST)   
        tipos = {'Viaje':Viaje,'Usuario': Usuario , 'form': forms }
        if forms.is_valid():
            forms.save()
            return redirect('tickets_url')
    return render(request, 'tickets/add_tickets.html',tipos )

def actualizar_ticket(request, id):
    Viaje = Viajes.objects.all()
    tickets = Tickets.objects.get(id=id)
    Usuario = Usuarios.objects.raw('SELECT * from usuarios where tipo_de_persona = 1;')
    if(request.method == 'GET'):
        forms = TicketsForm(instance= tickets)
        tipos = {'Viaje':Viaje,'Usuario': Usuario , 'form': forms}
    else:
        forms = TicketsForm(request.POST,instance= tickets)   
        tipos = {'Viaje':Viaje,'Usuario': Usuario , 'form': forms }
        if forms.is_valid():
            forms.save()
            return redirect('tickets_url')
    return render(request, 'tickets/update_tickets.html',tipos )

def borrar_ticket(request,id):
    tickets = Tickets.objects.get(id=id)
    tickets.delete()
    return redirect('tickets_url')