from django import forms
from .models import Camion, Viaje, Chofer

#Formulario para dar de alta o modificar la informacion de una unidad
class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['patente', 'modelo', 'tipo_unidad', 'chofer']

#Formulario para dar de alta o modificar la informacion de un viaje
class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['origen', 'destino', 'estado', 'camion']

#Formulario para dar de alta o modificar la informacion de un chofer
class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = ['nombre', 'apellido', 'celular', 'mail', 'cuit', 'legajo']