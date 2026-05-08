from django import forms
from .models import Mensaje

#Formulario para enviar un mensaje
class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'cuerpo']