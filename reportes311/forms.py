# importa los formulaios de django
from django import forms
from .models import Solicitud, Seguimiento


# se crea una clase para el formulario de solicitudes
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        # se crean los campos del formulario
        fields = '__all__'
        
class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        # se crean los campos del formulario
        fields = '__all__'


