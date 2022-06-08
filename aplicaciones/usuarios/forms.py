from dataclasses import fields
from django import forms
from .models import Usuarios

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ["nombre", "apellido", "telefono", "correo", "edad", "tipo_de_documento", "numero_de_documento", "rh"]
