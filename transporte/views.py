from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Camion, Viaje
from .forms import CamionForm, ViajeForm, ChoferForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

#Pagina de bienvenida
def home(request):
    return render(request, 'home.html')

#Quienes somos
def about(request):
    return render(request, 'about.html')

#MENU PRINCIPAL
#Contador de viajes completados o pendientes del total de las unidades
@login_required
def index(request):
    completados = Viaje.objects.filter(estado='Completado').count()
    pendientes = Viaje.objects.filter(estado='Pendiente').count()
    return render(request, 'index.html', {
        'completados': completados,
        'pendientes': pendientes,
    })

#Categoria de camiones
@login_required
def tipo_camion(request, tipo):
    patente = request.GET.get('patente', '')
    camiones = Camion.objects.filter(tipo_unidad=tipo)
    #Busqueda por patente
    if patente:
        camiones = camiones.filter(patente__icontains=patente)
    return render(request, 'tipo_camion.html', {
        'camiones': camiones,
        'tipo': tipo,
        'patente': patente,
    })

#Informacion completa de cada unidad
@login_required
def detalle_camion(request, pk):
    camion = get_object_or_404(Camion, pk=pk)
    completados = camion.viajes.filter(estado='Completado').count()
    pendientes = camion.viajes.filter(estado='Pendiente').count()
    return render(request, 'detalle_camion.html', {
        'camion': camion,
        'completados': completados,
        'pendientes': pendientes,
    })

#Alta de unidades 
class AgregarCamionView(LoginRequiredMixin, CreateView):
    model = Camion
    form_class = CamionForm
    template_name = 'agregar_camion.html'
    success_url = reverse_lazy('index')

#Editor de unidades 
class EditarCamionView(LoginRequiredMixin, UpdateView):
    model = Camion
    form_class = CamionForm
    template_name = 'agregar_camion.html'

    def get_success_url(self):
        return reverse_lazy('tipo_camion', kwargs={'tipo': self.object.tipo_unidad})

#Eliminar camion 
class EliminarCamionView(LoginRequiredMixin, DeleteView):
    model = Camion
    template_name = 'eliminar_camion.html'
    success_url = reverse_lazy('index')

    #Editor de viajes 
class EditarViajeView(LoginRequiredMixin, UpdateView):
    model = Viaje
    form_class = ViajeForm
    template_name = 'agregar_viaje.html'
    success_url = reverse_lazy('index')

#Detalle de viaje 
class DetalleViajeView(LoginRequiredMixin, DetailView):
    model = Viaje
    template_name = 'detalle_viaje.html'
    context_object_name = 'viaje'

#Alta de viajes
@login_required
def agregar_viaje(request):
    form = ViajeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'agregar_viaje.html', {'form': form})

#Eliminar viaje
@login_required
def eliminar_viaje(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)
    if request.method == 'POST':
        viaje.delete()
        return redirect('index')
    return render(request, 'eliminar_viaje.html', {'viaje': viaje})

#Alta de choferes
@login_required
def agregar_chofer(request):
    form = ChoferForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'agregar_chofer.html', {'form': form})

#Listado de viajes en route pages/
@login_required
def lista_viajes(request):
    viajes = Viaje.objects.all()
    return render(request, 'lista_viajes.html', {'viajes': viajes})