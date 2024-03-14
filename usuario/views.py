from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash, logout, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import UserExtension
from .forms import FormularioRegistro, FormularioCambiarContraseña, FormularioEditarPerfil



def crear_usuario(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form_registro = FormularioRegistro(request.POST)
        if form_registro.is_valid():
            form_registro.save()
            return redirect('home')
    else:
        form_registro = FormularioRegistro()

    return render(request, 'usuario/crear_usuario.html', { 'form_registro' : form_registro })

def editar_contraseña(request):
    if request.method == 'POST':
        form = FormularioCambiarContraseña(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña ha sido actualizada correctamente')
            return redirect('home')
        else:
            messages.error(request, 'Por favor corrige el error abajo.')
    else:
        form = FormularioCambiarContraseña(request.user)
    return render(request, 'usuario/editar_pass.html', {'form': form})

@login_required
def ver_perfil(request):
    return render(request, 'usuario/ver_perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        formulario_editar_perfil = FormularioEditarPerfil(request.POST, request.FILES)

        if formulario_editar_perfil.is_valid():
            datos = formulario_editar_perfil.cleaned_data
            request.user.email = datos['email']
            request.user.first_name = datos['nombre']
            request.user.last_name = datos['apellido']

            if datos['avatar'] == False:
                request.user.userextension.avatar = None
            elif datos['avatar'] != None:
                request.user.userextension.avatar = datos['avatar']

            request.user.userextension.descripcion = datos['descripcion']
            request.user.userextension.link = datos['link']

            request.user.save()
            request.user.userextension.save()

            return redirect('ver_perfil')
    else:
        form_editar_perfil = FormularioEditarPerfil(
            initial={
                'email' : request.user.email,
                'first_name' : request.user.first_name,
                'last_name' : request.user.last_name,
                'avatar' : request.user.userextension.avatar,
                'descripcion' : request.user.userextension.descripcion,
                'link' : request.user.userextension.link,
            }
        )
    return render(request, 'usuario/editar_perfil.html', { 'form_editar_perfil' : form_editar_perfil })

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form_login = AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            user = form_login.get_user()
            login(request, user)
            usuario_perfil, es_nuevo_usuarioperfil = UserExtension.objects.get_or_create(user=request.user)
            return redirect('home')
    else:
        form_login = AuthenticationForm()

    return render(request, 'usuario/iniciar_sesion.html', { 'form_login' : form_login })

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')