from django.urls import path
from aplicaciones.usuarios.views import usuario_urls, insertar_usuarios, editar_usuarios, borrar_usuarios,graficar_usuarios

urlpatterns = [
    path('usuarios', usuario_urls , name="usuario_urls"),
    path('graficar', graficar_usuarios , name="graficar_usuarios"),
    path('insertar_usuarios', insertar_usuarios, name="insertar_usuarios"),
    path('editar_usuarios/<int:id>', editar_usuarios, name="editar_usuarios"),
    path('borrar_usuarios/<int:id>', borrar_usuarios, name="borrar_usuarios"),

]
