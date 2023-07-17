# Description: URLS de la aplicación reportes311
from django.urls import path
from .import views
#. import views

# para cargar imagenes
from django.conf import settings
from django.contrib.staticfiles.urls import static



# URLS de la aplicación reportes311
urlpatterns = [
    
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    
# interfaces de creacion de solicitudes   
# nombres de las urls para cada interfaz  "solicitudes", "crear", "editar
    path('solicitudes/index', views.solicitudes, name='solicitudes'),
    path('solicitudes/crear', views.crear, name='crear'),
    path('solicitudes/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('solicitudes/editar/<int:id>', views.editar, name='editar'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
