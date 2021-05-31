#importar modelos
from veterinariaapp.models.Usuarios import Usuarios

#importar forms
from veterinariaapp.forms.UsuariosForm import UsuariosForm

# paquetes y librerias
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import time

nombreUsuario=None

def vw_usuarios_list(request):
    if "session_usuario" in request.session:
        vwUsuarios = Usuarios.objects.all().order_by('usuario')
        global nombreUsuario

        if request.POST.get('usuario'):
            nombreUsuario = request.POST.get('usuario')
            vwUsuarios = vwUsuarios.filter(usuario__icontains=nombreUsuario)
        else:
            nombreUsuario = None

        return render(request,'veterinariaapp/usuarios_list.html',{'vwUsuarios':vwUsuarios,'nombreUsuario':nombreUsuario})
    else:
        return redirect('url_login')



#Editar usuarios
def vw_usuarios_edit(request,pk):
    if "session_usuario" in request.session:
        messages.info(request, 'Editar Usuario')
        usuario_vw = get_object_or_404(Usuarios, pk=pk)
        if request.method == "POST":
            form = UsuariosForm(request.POST, instance=usuario_vw)
            if form.is_valid():
                form.save()
                us = Usuarios.objects.get(usuario=request.session['session_usuario'])
                messages.info(request, 'El usuario se edito correctamente')

                return redirect('url_usuarios_list')
        else:
            form = UsuariosForm(instance=usuario_vw)
        return render(request, 'veterinariaapp/usuarios_edit.html', {'form': form, 'usuario_vw': usuario_vw})
    else :
        return redirect('url_login')

#Agregar usuarios principal
def vw_usuarios_new_general(request):
    form = UsuariosForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'El usuario se agregó correctamente')
        return redirect('url_usuarios_new_general')
    else:
        form = UsuariosForm()
        return render(request, 'veterinariaapp/usuarios_new.html', {'form': form } )

#Agregar usuarios
def vw_usuarios_new(request):
    if "session_usuario" in request.session:
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El usuario se agregó correctamente')
            return redirect('url_usuarios_list')
        else:

            form = UsuariosForm()
            return render(request, 'veterinariaapp/usuarios_edit.html', {'form': form } )
    else :
        return redirect('url_login')

#Eliminar usuarios
def vw_usuarios_delete(request,pk):
    if "session_usuario" in request.session:
        try:
            usuario = Usuarios.objects.filter(usuario=pk)
            usuario.delete()
            messages.success(request, 'El usuario se eliminó Correctamente')
            return redirect('url_usuarios_list')
        except:
            print("Error...")
            messages.error(request, 'El usuario que quiere eliminar tiene dependencias asociadas')
            return redirect('url_usuarios_list')
    else :
        return redirect('url_login')















