from django.db import models

# Create your models here.

#Opciones de tipos de camiones
TIPOS_CAMION = [
    ('Chasis', 'Chasis'),
    ('Articulado Semirremolque','Articulado Semirremolque'),
    ('Articulado Britén', 'Articulado Britén'),
]

#Modelo de informacion obligatoria de los choferes    
class Chofer(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)
    mail =  models.EmailField(blank=True, null=True)
    cuit = models.CharField(max_length=20)
    legajo = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

#Modelo de informacion obligatoria de las unidades    
class Camion(models.Model):
    patente = models.CharField(max_length=10)
    modelo = models.CharField(max_length=50)
    tipo_unidad = models.CharField(max_length=50)
    chofer = models.ForeignKey(Chofer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.patente

#Modelo de informacion sobre los viajes realizados o pendientes    
class Viaje(models.Model):
    ESTADOS = [
        ('Completado','Completado'),
        ('Pendiente','Pendiente'),
    ]
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE, related_name='viajes')

    def __str__(self):
        return f'{self.origen} → {self.destino}'
