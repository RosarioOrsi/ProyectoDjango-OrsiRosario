from django.db import models
from django.conf import settings

#Modelo de mensajes entre usuarios
class Mensaje(models.Model):
    #Usuario que envia el mensaje
    remitente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mensajes_enviados')
    #Usuario que recibe el mensaje
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    #Asunto del mensaje
    asunto = models.CharField(max_length=200)
    #Contenido del mensaje
    cuerpo = models.TextField()
    #Fecha de envio (se completa automaticamente)
    fecha = models.DateTimeField(auto_now_add=True)
    #Si el destinatario lo leyo o no
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.remitente} → {self.destinatario}: {self.asunto}"

    class Meta:
        ordering = ['-fecha']
