from django.contrib import admin

# Register your models here.
from .models import Solicitud,Seguimiento

# Register your models here.

admin.site.register(Solicitud)
admin.site.register(Seguimiento)
