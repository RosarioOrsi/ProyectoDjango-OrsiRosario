from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import PerfilCreateForm, PerfilChangeForm

#Vista de registro
def register(request):
    form = PerfilCreateForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect ('index')
    return render(request, "accounts/register.html",{'form':form})


# Vista de login:
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            # Si las credenciales son incorrectas, mostramos un error
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'accounts/login.html')


# Vista de logout: 
def logout_view(request):
    logout(request)
    return redirect('index')


# Vista de detalle de perfil: 
@login_required
def perfil_detail(request):
    return render(request, 'accounts/profile_detail.html')


# Vista de edición de perfil: 
@login_required
def perfil_change(request):
    form = PerfilChangeForm(request.POST or None, request.FILES or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('perfil_detail')
    return render(request, 'accounts/profile_change.html', {'form': form})


# Vista de cambio de contraseña:
@login_required
def password_change(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if form.is_valid():
        user = form.save()
        # Evita que se cierre la sesión al cambiar la contraseña
        update_session_auth_hash(request, user)
        messages.success(request, 'Contraseña actualizada correctamente.')
        return redirect('perfil_detail')
    return render(request, 'accounts/password_change.html', {'form': form})