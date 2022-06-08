from django.urls import path
from aplicaciones.inicio.views import inicio_urls, bioseguridad, servicio_cliente, decreto

urlpatterns = [
    path('', inicio_urls , name="inicio_urls"),
    path('bioseguridad', bioseguridad, name="bioseguridad"),
    path('decreto_1168', decreto, name="decreto_1168"),
    path('servicio_al_cliente', servicio_cliente, name="servicio_al_cliente"),
    # path('inicio', inicio , name='inicio')
]