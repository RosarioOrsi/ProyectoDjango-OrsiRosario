from django.urls import path
from . import views

urlpatterns = [
    #Bandeja de entrada
    path('', views.bandeja_entrada, name='bandeja_entrada'),
    #Mensajes enviados
    path('enviados/', views.mensajes_enviados, name='mensajes_enviados'),
    #Enviar mensaje nuevo
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    #Ver detalle de un mensaje
    path('mensaje/<int:pk>/', views.detalle_mensaje, name='detalle_mensaje'),
    #Eliminar mensaje
    path('eliminar/<int:pk>/', views.eliminar_mensaje, name='eliminar_mensaje'),
]