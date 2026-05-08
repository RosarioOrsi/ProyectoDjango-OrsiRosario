from django.urls import path
from .import views

urlpatterns = [
    # Registro de nuevo usuario
    path('register/', views.register, name='register'),

    # Login y logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Perfil: ver, editar y cambiar contraseña
    path('perfil/', views.perfil_detail, name='perfil_detail'),
    path('perfil/editar/', views.perfil_change, name='perfil_change'),
    path('perfil/cambiar-password/', views.password_change, name='password_change'),
]
