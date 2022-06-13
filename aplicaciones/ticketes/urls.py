from django.urls import path
from aplicaciones.ticketes.views import tickets_url,insertar_ticket

urlpatterns = [
    path('tickets', tickets_url , name="tickets_url"),
    path('insertar_ticket', insertar_ticket, name="insertar_ticket"),
    # path('inicio', inicio , name='inicio')
]