# importa los formulaios de django
from django import forms
from .models import Solicitud

# se crea una clase para el formulario de solicitudes
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        # se crean los campos del formulario
        fields = '__all__'
        



