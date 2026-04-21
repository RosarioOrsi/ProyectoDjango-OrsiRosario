from django.contrib import admin
from .models import Camion, Viaje, Chofer
# Register your models here.

#Registramos los modelos para que sean visibles en el panel de administracion
admin.site.register(Camion)
admin.site.register(Viaje)
admin.site.register(Chofer)