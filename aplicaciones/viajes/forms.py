from dataclasses import fields
from django import forms
from .models import Viajes

class ViajesForm(forms.ModelForm):
    class Meta:
        model = Viajes
        fields = '__all__'