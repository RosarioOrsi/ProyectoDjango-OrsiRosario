from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Mensaje
from .forms import MensajeForm

#Lista de mensajes recibidos
@login_required
def bandeja_entrada(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'mensajes/bandeja_entrada.html', {'mensajes': mensajes})

#Lista de mensajes enviados
@login_required
def mensajes_enviados(request):
    mensajes = Mensaje.objects.filter(remitente=request.user)
    return render(request, 'mensajes/mensajes_enviados.html', {'mensajes': mensajes})

#Enviar mensaje nuevo
@login_required
def enviar_mensaje(request):
    form = MensajeForm(request.POST or None)
    if form.is_valid():
        mensaje = form.save(commit=False)
        mensaje.remitente = request.user
        mensaje.save()
        return redirect('bandeja_entrada')
    return render(request, 'mensajes/enviar_mensaje.html', {'form': form})

#Ver detalle de un mensaje
@login_required
def detalle_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if mensaje.destinatario == request.user:
        mensaje.leido = True
        mensaje.save()
    return render(request, 'mensajes/detalle_mensaje.html', {'mensaje': mensaje})

#Eliminar mensaje
@login_required
def eliminar_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if request.method == 'POST':
        mensaje.delete()
        return redirect('bandeja_entrada')
    return render(request, 'mensajes/eliminar_mensaje.html', {'mensaje': mensaje})