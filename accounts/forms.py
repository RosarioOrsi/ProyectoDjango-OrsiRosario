from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Perfil

# Validar contraseña
def validar_password(value):
    errores = []
    if len(value) < 8:
        errores.append('al menos 8 caracteres')
    if not any(c.isupper() for c in value):
        errores.append('al menos una mayúscula')
    if not any(c.islower() for c in value):
        errores.append('al menos una minúscula')
    if not any(c.isdigit() for c in value):
        errores.append('al menos un número')
    if not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in value):
        errores.append('al menos un carácter especial (!@#$%^&*...)')
    if errores:
        raise ValidationError(f'La contraseña debe contener: {", ".join(errores)}.')


# Formulario de registro
class PerfilCreateForm(UserCreationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        help_text='Solo letras, números y los caracteres @/./+/-/_',
        max_length=150,
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        validators=[validar_password],
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput,
        help_text='Ingresá la misma contraseña para verificar.',
    )

    class Meta:
        model = Perfil
        fields = ['username', 'email', 'password1', 'password2']
   
#Editar perfil
class PerfilChangeForm(forms.ModelForm):
    class Meta:
        model = Perfil
        # No incluye password — el cambio de contraseña va en su propia vista
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar', 'bio', 'fecha_de_nacimiento']
