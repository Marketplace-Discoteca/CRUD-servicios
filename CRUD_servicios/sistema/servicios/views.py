from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Servicio
from .forms import ServicioForm

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def servicios(request):
    servicios = Servicio.objects.all()  # Corregido 'objets' a 'objects'
    return render(request, 'servicios/index.html', {'servicios': servicios})  # También pasa la variable correcta

def crear(request):
    formulario = ServicioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('servicios')
    return render(request, 'servicios/crear.html', {'formulario': formulario})

def editar(request, id):
    servicio = Servicio.objects.get(id=id)
    formulario = ServicioForm(request.POST or None, request.FILES or None, instance=servicio)  # Pasar el objeto existente

    if formulario.is_valid():  # Verifica si el formulario es válido
        formulario.save()  # Guarda los cambios en el modelo
        return redirect('servicios')  # Redirige a la lista de servicios después de guardar

    return render(request, 'servicios/editar.html', {'formulario': formulario})  # Renderiza el formulario para editar


def eliminar(request, id):
    servicios = Servicio.objects.get(id=id)
    servicios.delete()
    return redirect('servicios')
