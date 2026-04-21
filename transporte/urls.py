from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tipo/<str:tipo>/', views.tipo_camion, name='tipo_camion'),
    path('camion/<int:pk>/', views.detalle_camion, name='detalle_camion'),
    path('agregar-camion/', views.agregar_camion, name='agregar_camion'),
    path('editar-camion/<int:pk>/', views.editar_camion, name='editar_camion'),
    path('agregar-viaje/', views.agregar_viaje, name='agregar_viaje'),
    path('agregar-chofer/', views.agregar_chofer, name='agregar_chofer'),
  
]