from veterinariaapp.models.Usuarios import Usuarios
from django.shortcuts import render, redirect

from django.http.response import HttpResponse
from django.contrib import messages

def vw_login(request):

    if "session_usuario" in request.session:
        return redirect('url_inicio')
    else:
        if request.method == "POST":
            try:
                us = Usuarios.objects.get(usuario=request.POST['usuario'])
                if us.status == 1:
                    if us.password == request.POST['password']:
                        if us.tipousuario==1:
                            request.session['session_usuario'] = us.usuario
                            request.session['session_tipousuario'] = us.tipousuario

                            return redirect('url_inicioAdministrador')
                        else:
                            request.session['session_usuario'] = us.usuario
                            request.session['session_tipousuario'] = us.tipousuario
                            return redirect('url_inicioCliente')

                    else:
                        messages.error(request, 'Contraseña Incorrecta')
                        return redirect('url_login')
                else:
                    messages.error(request, 'Usuario Inactivo')
                    return redirect('url_login')
            except Usuarios.DoesNotExist:
                messages.error(request, 'Usuario Incorrecto')
                return redirect('url_login')
        else:
            return render(request, 'veterinariaapp/login.html', {})

def vw_inicioCliente(request):
    if "session_usuario" in request.session:
        return render(request, 'veterinariaapp/homeCliente.html', {})
    else:
       return redirect('url_login')

def vw_inicioAdministrador(request):
    if "session_usuario" in request.session:
        return render(request, 'veterinariaapp/homeAdministrador.html', {})
    else:
        return redirect('url_login')


def vw_inicio(request):
    return render(request, 'veterinariaapp/index.html', {})

def vw_mascotas(request):
    return render(request, 'veterinariaapp/mascotas.html', {})



def vw_salir(request):
    try:
        del request.session['session_usuario']
        del request.session['session_tipousuario']
    except KeyError:
        print('No existe la sesion...')
    return redirect('url_login')