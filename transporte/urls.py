from django.urls import path
from . import views

urlpatterns = [
    #Pagina de bienvenida
    path('', views.home, name='home'),
    #Quienes somos
    path('about/', views.about, name='about'),
    #Menu principal 
    path('dashboard/', views.index, name='index'),
    #Lista de camiones por categoria
    path('tipo/<str:tipo>/', views.tipo_camion, name='tipo_camion'),
    #Detalle de camion en especifico
    path('camion/<int:pk>/', views.detalle_camion, name='detalle_camion'),
    #Alta de unidad 
    path('agregar-camion/', views.AgregarCamionView.as_view(), name='agregar_camion'),
    #Edicion de unidad 
    path('editar-camion/<int:pk>/', views.EditarCamionView.as_view(), name='editar_camion'),
    #Eliminar unidad
    path('eliminar-camion/<int:pk>/', views.EliminarCamionView.as_view(), name='eliminar_camion'),
    #Alta de viaje
    path('agregar-viaje/', views.agregar_viaje, name='agregar_viaje'),
    #Eliminar viaje
    path('eliminar-viaje/<int:pk>/', views.eliminar_viaje, name='eliminar_viaje'),
    #Edicion de viaje 
    path('editar-viaje/<int:pk>/', views.EditarViajeView.as_view(), name='editar_viaje'),
    #Detalle de viaje 
    path('viaje/<int:pk>/', views.DetalleViajeView.as_view(), name='detalle_viaje'),
    #Listado de viajes - route pages/
    path('pages/', views.lista_viajes, name='lista_viajes'),
    #Detalle de viaje - route pages/
    path('pages/<int:pk>/', views.DetalleViajeView.as_view(), name='detalle_viaje_pages'),
    #Alta de chofer
    path('agregar-chofer/', views.agregar_chofer, name='agregar_chofer'),
]