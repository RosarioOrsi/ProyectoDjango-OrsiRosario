from django.urls import path
from . import views

urlpatterns = [
    #Menu principal
    path('', views.index, name='index'),
    #Lista de camiones por categoria
    path('tipo/<str:tipo>/', views.tipo_camion, name='tipo_camion'),
    #Detalle de camion en especifico
    path('camion/<int:pk>/', views.detalle_camion, name='detalle_camion'),
    #Alta de unidad
    path('agregar-camion/', views.agregar_camion, name='agregar_camion'),
    #Edicion de la informacion de una de las unidades preexistentes
    path('editar-camion/<int:pk>/', views.editar_camion, name='editar_camion'),
    #Alta de viaje
    path('agregar-viaje/', views.agregar_viaje, name='agregar_viaje'),
    #Ata de chofer
    path('agregar-chofer/', views.agregar_chofer, name='agregar_chofer'),
  
]