# URLs principales del proyecto
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transporte.urls')),
    
    # Conecta todas las URLs de la app accounts
    path('accounts/', include('accounts.urls')),

    # CKEditor
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Mensajería
    path('mensajes/', include('mensajes.urls')),
]
 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)