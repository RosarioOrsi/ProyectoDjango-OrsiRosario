# ProyectoDjango-OrsiRosario
Primer entrega del tp final
#########################
##Empresa de Transporte##
#########################

Este proyecto es una aplicación web desarrollada en Django . La idea fue crear un sistema de gestión para una empresa de transporte, donde se pueden llevar un control de los camiones, choferes y viajes que se van realizando o aun se encuentran pendientes.

############################
##¿Qué hace la aplicación?##
############################

Esta página permite registrar y almacenar la información correspondiente a cada tipo de camión, junto con los datos de los choferes asignados. Su finalidad es mejorar el control interno y facilitar el acceso a la información cuando sea requerida.

###########################
##Herramientas utilizadas##
##########################

- Python 3.14
- Django 6.0
- SQLite (base de datos por defecto de Django)
- HTML y CSS

######################################
##Cómo instalar y correr el proyecto##
######################################

1. Clonar el repositorio**
```bash
git clone https://github.com/RosarioOrsi/ProyectoDjango-OrsiRosario.git
cd ProyectoDjango-OrsiRosario
```

2. Crear y activar el entorno virtual**
```bash
python -m venv Entorno
.\Entorno\Scripts\activate
```

3. Instalar las dependencias**
```bash
pip install -r requirements.txt
```

4. Aplicar las migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Correr el servidor**
```bash
python manage.py runserver
```

6. Abrir en el navegador
http://127.0.0.1:8000/

#####################################
##¿Como probar las funcionalidades?##
#####################################

- Desde el menú principal es posible visualizar los contadores de viajes y seleccionar el tipo de camión correspondiente.
- Para incorporar un nuevo chofer, utilice el botón + Chofer disponible en el menú principal.
- Para registrar una nueva unidad, ingrese a la categoría de camión correspodiente y seleccione + Agregar Unidad.
- Para cargar un viaje, utilice el botón + Viaje ubicado en el menú principal.
- El buscador por patente se encuentra habilitado dentro de cada tipo de camión para una identificación rápida.
- Al seleccionar Ver más, se accede al detalle completo de la unidad, incluyendo información del chofer asignado y el historial de viajes.

###########################
##Estructura del proyecto##
###########################

PROYECTO_DJANGO/
├── Empresa_de_Transporte/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── transporte/
│   ├── migrations/
│   ├── templates/
│   │   ├── agregar_camion.html
│   │   ├── agregar_chofer.html
│   │   ├── agregar_viaje.html
│   │   ├── base.html
│   │   ├── detalle_camion.html
│   │   ├── index.html
│   │   └── tipo_camion.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md