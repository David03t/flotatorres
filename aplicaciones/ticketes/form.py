from dataclasses import fields
from django import forms
from .models import Tickets

class TicketsForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = '__all__'