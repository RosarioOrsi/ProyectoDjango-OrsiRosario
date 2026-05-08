from django.contrib import admin
from .models import Mensaje

#Registro del modelo Mensaje en el admin
admin.site.register(Mensaje)