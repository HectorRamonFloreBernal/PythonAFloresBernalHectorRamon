from django.shortcuts import render, redirect
from django.http import HttpResponse

# importar el modelo de la calse Solicitud de models.py
from  .models import Solicitud, Seguimiento

# importa los formularios de django de solicitdForm
from .forms import SolicitudForm, SeguimientoForm


# Create your views here.

# funcion vista para la pagina de inicio
def inicio(request):
    return render(request, "paginas/inicio.html")
# funcion vista para la pagina de nosotros
def nosotros(request):
    return render(request, "paginas/nosotros.html")


# funcion vista para la pagina de Solicitudes
# que permite mostrar todas las solicitudes de la base de datos
def solicitudes(request):
    # obtener todas las solicitudes de la base de datos
    solicitudes = Solicitud.objects.all()
    # print(solicitudes)
    # manda solocitudes a la plantilla index_solicitud.html
    return render(request, "reportes/index_solicitud.html", {"solicitudes":solicitudes})

# funcion vista para la pagina de crear solicitud
def crear(request):
    # crea un formulario vacio para que el usuario lo llene y despues validar si es correcto
    formulario = SolicitudForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        # guarda el formulario en la base de datos
        formulario.save()
        # redirecciona a la pagina de solicitudes
        return redirect('solicitudes')        
    return render(request, "reportes/crear_solicitud.html", {'formulario':formulario})


# funcion vista para la pagina de editar solicitud
def editar(request, id):
    solicitud = Solicitud.objects.get(id=id)
    formulario = SolicitudForm(request.POST or None, request.FILES or None, instance=solicitud)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('solicitudes')
    return render(request, "reportes/editar_solicitud.html", {'formulario':formulario})

# funcion vista para la pagina de eliminar solicitud
def eliminar(request, id):
    solicitud = Solicitud.objects.get(id=id)
    solicitud.delete()
    return redirect('solicitudes')
    # return render(request, "reportes/eliminar_solicitud.html")
    
# ---------------------  seguimiento

def seguimientos(request):
    # obtener todas los seguimientos de la base de datos
    seguimiento = Seguimiento.objects.all()
    return render(request, "reportes/index_seguimiento.html", {"seguimiento":seguimiento})

# funcion vista para la pagina de crear solicitud
def crearSeg(request):
    # crea un formulario vacio para que el usuario lo llene y despues validar si es correcto
    formulario1 = SeguimientoForm(request.POST or None, request.FILES or None)
    if formulario1.is_valid():
        # guarda el formulario en la base de datos
        formulario1.save()
        # redirecciona a la pagina de solicitudes
        return redirect('seguimiento')        
    return render(request, "reportes/crear_seg.html", {'formulario1':formulario1})

# funcion vista para la pagina de editar solicitud
def editarSeg(request, id):
    seguimiento = Seguimiento.objects.get(id=id)
    formulario1 = SeguimientoForm(request.POST or None, request.FILES or None, instance=seguimiento)
    if formulario1.is_valid() and request.POST:
        formulario1.save()
        return redirect('seguimiento')
    return render(request, "reportes/editar_seg.html", {'formulario1':formulario1})