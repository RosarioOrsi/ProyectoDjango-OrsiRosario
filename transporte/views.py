from django.shortcuts import render, redirect, get_object_or_404
from .models import Camion, Viaje
from .forms import CamionForm, ViajeForm, ChoferForm

def index(request):
    completados = Viaje.objects.filter(estado='Completado').count()
    pendientes = Viaje.objects.filter(estado='Pendiente').count()
    return render(request, 'index.html', {
        'completados': completados,
        'pendientes': pendientes,
    })

def tipo_camion(request, tipo):
    patente = request.GET.get('patente', '')
    camiones = Camion.objects.filter(tipo_unidad=tipo)
    if patente:
        camiones = camiones.filter(patente__icontains=patente)
    return render(request, 'tipo_camion.html', {
        'camiones': camiones,
        'tipo': tipo,
        'patente': patente,
    })

def detalle_camion(request, pk):
    camion = get_object_or_404(Camion, pk=pk)
    completados = camion.viajes.filter(estado='Completado').count()
    pendientes = camion.viajes.filter(estado='Pendiente').count()
    return render(request, 'detalle_camion.html', {
        'camion': camion,
        'completados': completados,
        'pendientes': pendientes,
    })

def agregar_camion(request):
    form = CamionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'agregar_camion.html', {'form': form})

def editar_camion(request, pk):
    camion = get_object_or_404(Camion, pk=pk)
    form = CamionForm(request.POST or None, instance=camion)
    if form.is_valid():
        form.save()
        return redirect('tipo_camion', tipo=camion.tipo_unidad)
    return render(request, 'agregar_camion.html', {'form': form, 'editar': True})

def agregar_viaje(request):
    form = ViajeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'agregar_viaje.html', {'form': form})

def agregar_chofer(request):
    form = ChoferForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'agregar_chofer.html', {'form': form})