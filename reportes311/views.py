from django.shortcuts import render, redirect
from django.http import HttpResponse

# Importar el modelo del logion de django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Importar el modelo de la calse Solicitud de models.py
from  .models import Solicitud, Seguimiento

# Importa los formularios de django de solicitdForm
from .forms import SolicitudForm, SeguimientoForm

# Create your views here.

# Funcion vista para la pagina de inicio
# Oculta la vista, hasta que un usuario valido inicie cencion 
@login_required
def inicio(request):
    return render(request, "paginas/inicio.html")

# funcion vista para la pagina de nosotros
def nosotros(request):
    return render(request, "paginas/nosotros.html")

# -----------------  Solicitudes ----------------------------------------------

# Funcion vista para la pagina de Solicitudes
# Que permite mostrar todas las solicitudes de la base de datos

def solicitudes(request):
    # obtener todas las solicitudes de la base de datos
    solicitudes = Solicitud.objects.all() 
    # manda solocitudes a la plantilla index_solicitud.html
    return render(request, "reportes/index_solicitud.html", {"solicitudes":solicitudes})

# Funcion vista para la pagina de crear solicitud
def crear(request):
    # crea un formulario vacio para que el usuario lo llene y despues validar si es correcto
    formulario = SolicitudForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        # guarda el formulario en la base de datos
        formulario.save()
        # redirecciona a la pagina de solicitudes
        return redirect('solicitudes')        
    return render(request, "reportes/crear_solicitud.html", {'formulario':formulario})

# Funcion vista para la pagina de editar solicitud
def editar(request, id):
    solicitud = Solicitud.objects.get(id=id)
    formulario = SolicitudForm(request.POST or None, request.FILES or None, instance=solicitud)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('solicitudes')
    return render(request, "reportes/editar_solicitud.html", {'formulario':formulario})

# Funcion vista para la pagina de eliminar solicitud
def eliminar(request, id):
    solicitud = Solicitud.objects.get(id=id)
    solicitud.delete()
    return redirect('solicitudes')
    
# ---------------------  seguimiento  ----------------------------------------------

def seguimientos(request):
    # obtener todas los seguimientos de la base de datos
    seguimientos = Seguimiento.objects.all()
    return render(request, "reportes/index_seguimiento.html", {"seguimientos":seguimientos})

# Funcion vista para la pagina de crear solicitud
def crearSeg(request):
    # crea un formulario vacio para que el usuario lo llene y despues validar si es correcto
    formulario = SeguimientoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        # guarda el formulario en la base de datos
        formulario.save()
        # redirecciona a la pagina de solicitudes
        return redirect('seguimiento')        
    return render(request, "reportes/crear_seg.html", {'formulario':formulario})

# Funcion vista para la pagina de editar solicitud
def editarSeg(request, id):
    seguimiento = Seguimiento.objects.get(id=id)
    formulario = SeguimientoForm(request.POST or None, request.FILES or None, instance=seguimiento)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('seguimiento')
    return render(request, "reportes/editar_seg.html", {'formulario':formulario})

# Funcion vista para la pagina de eliminar solicitud
def eliminarSeg(request, id):
    seguimiento = Seguimiento.objects.get(id=id)
    seguimiento.delete()
    return redirect('seguimientos')
      
#--------------------------------------------------------------------

def salir(request):
    logout(request)
    return redirect('/')
