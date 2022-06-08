from django.urls import path
from aplicaciones.viajes.views import viajes_url

urlpatterns = [
    path('viajes', viajes_url , name="inicio_urls"),
    # path('inicio', inicio , name='inicio')
]