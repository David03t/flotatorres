from django.urls import path
from aplicaciones.viajes.views import viajes_url, insertar_viajes, actualizar_viajes, borrar_viajes

urlpatterns = [
    path('viajes', viajes_url , name="viajes_url"),
    path('insertar_viajes', insertar_viajes , name="insertar_viajes"),
    path('editar_viajes/<int:id>', actualizar_viajes , name="actualizar_viajes"),
    path('borrar_viajes/<int:id>', borrar_viajes , name="borrar_viajes"),
    # path('inicio', inicio , name='inicio')
]