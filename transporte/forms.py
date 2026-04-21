from django import forms
from .models import Camion, Viaje, Chofer

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['patente', 'modelo', 'tipo_unidad', 'chofer']

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['origen', 'destino', 'estado', 'camion']

class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = ['nombre', 'apellido', 'celular', 'mail', 'cuit', 'legajo']