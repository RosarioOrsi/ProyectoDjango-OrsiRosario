#ProyectoDjango-OrsiRosario
Entrega final del TP

###################################
#Empresa de Transporte — Flota Sur#
###################################

Aplicación web desarrollada en Django para la gestión interna de una empresa de transporte. Permite llevar el control de camiones, choferes, viajes y mensajería interna entre usuarios.

##########################
#¿Qué hace la aplicación?#
##########################

- Registro y gestión de camiones por tipo (Chasis, Semirremolque, Bitrén)
- Alta, edición y eliminación de choferes
- Carga, edición y seguimiento de viajes con imagen y descripción
- Sistema de mensajería interna entre usuarios registrados
- Perfiles de usuario con avatar, biografía y cambio de contraseña
- Panel de administración de Django
- Autenticación completa: registro, login y logout

#########################
#Herramientas utilizadas#
#########################

- Python 3.14
- Django 6.0
- SQLite
- CKEditor
- HTML y CSS

####################################
#Cómo instalar y correr el proyecto#
####################################

1. Clonar el repositorio
```bash
git clone https://github.com/RosarioOrsi/ProyectoDjango-OrsiRosario.git
cd ProyectoDjango-OrsiRosario
```

2. Crear y activar el entorno virtual
```bash
python -m venv Entorno
.\Entorno\Scripts\activate
```

3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

4. Aplicar las migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Correr el servidor
```bash
python manage.py runserver
```

6. Abrir en el navegador: http://127.0.0.1:8000/

###################################
#¿Cómo probar las funcionalidades?#
###################################

- Registrarse o iniciar sesión para acceder al sistema
- Desde el Dashboard se ven los contadores de viajes completados y pendientes
- Desde Pages se accede al listado completo de viajes con "Leer más"
- Seleccionar un tipo de camión para ver las unidades registradas
- Usar "+ Agregar Unidad" para dar de alta un camión
- Usar "+ Viaje" para registrar un nuevo viaje con imagen y descripción
- En el detalle de cada camión se ve el historial de viajes con "Ver más"
- Usar "📬 Mensajes" en el navbar para acceder a la mensajería interna
- Desde el perfil se puede editar la información personal y cambiar la contraseña

#########################
#Estructura del proyecto#
#########################

```
PROYECTO_DJANGO/
├── accounts/
│   ├── migrations/
│   ├── templates/accounts/
│   │   ├── login.html
│   │   ├── password_change.html
│   │   ├── profile_change.html
│   │   ├── profile_detail.html
│   │   └── register.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── Empresa_de_Transporte/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── mensajes/
│   ├── migrations/
│   ├── templates/mensajes/
│   │   ├── bandeja_entrada.html
│   │   ├── detalle_mensaje.html
│   │   ├── eliminar_mensaje.html
│   │   ├── enviar_mensaje.html
│   │   └── mensajes_enviados.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── transporte/
│   ├── migrations/
│   ├── templates/
│   │   ├── about.html
│   │   ├── agregar_camion.html
│   │   ├── agregar_chofer.html
│   │   ├── agregar_viaje.html
│   │   ├── base.html
│   │   ├── detalle_camion.html
│   │   ├── detalle_viaje.html
│   │   ├── eliminar_camion.html
│   │   ├── eliminar_viaje.html
│   │   ├── home.html
│   │   ├── index.html
│   │   ├── lista_viajes.html
│   │   └── tipo_camion.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```