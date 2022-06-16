from django.urls import path
from aplicaciones.ticketes.views import tickets_url,insertar_ticket, actualizar_ticket , borrar_ticket

urlpatterns = [
    path('tickets', tickets_url , name="tickets_url"),
    path('insertar_ticket', insertar_ticket, name="insertar_ticket"),
    path('editar_ticket/<int:id>', actualizar_ticket, name="actualizar_ticket"),
    path('borrar_ticket/<int:id>', borrar_ticket, name="borrar_ticket"),
    # path('inicio', inicio , name='inicio')
]