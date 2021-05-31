
#importar modelos
from veterinariaapp.models.Mascotas import Mascotas
from veterinariaapp.models.Servicios import Servicios
from veterinariaapp.models.Usuarios import Usuarios
from veterinariaapp.models.Citas import Citas


# importar formulario
from veterinariaapp.forms.CitasForm import CitasForm
# paquetes y librerias
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import time
from django.contrib import messages


#Obtener citas agendadas
def citas_list(request):
    if "session_usuario" in request.session:
        usuarios = Usuarios.objects.all().order_by('usuario')
        mascotas = Mascotas.objects.all()
        servicios = Servicios.objects.all()
        citas = Citas.objects.all()

        return render(request, 'veterinariaapp/citas_list.html', {'citas':citas,
                                                                  'usuarios': usuarios,
                                                                  'mascotas': mascotas,
                                                                  'servicios':servicios,
                                                                          })
    else :
        return redirect('url_login')

#Agregar una cita
def cita_new(request):
    if "session_usuario" in request.session:
        messages.info(request, 'Nueva cita')
        usuarios = Usuarios.objects.all().order_by('usuario')
        mascotas = Mascotas.objects.all()
        servicios = Servicios.objects.all()

        form = CitasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_citas_list')
        else:
            form = CitasForm()
            return render(request, 'veterinariaapp/citas_edit.html', {'form': form,
                                                                      'usuarios':usuarios,
                                                                      'mascotas': mascotas,
                                                                      'servicios': servicios,
                                                                      })
    else :
        return redirect('url_login')

#Editar una cita
def cita_edit(request, pk):
    if "session_usuario" in request.session:
        messages.info(request, 'Editar venta de productos')
        usuarios = Usuarios.objects.all().order_by('usuario')

        cita = get_object_or_404(Citas, pk=pk)
        if request.method == "POST":
            form = CitasForm(request.POST, instance=cita)
            if form.is_valid():
                form.save()
                return redirect('url_citas_list')
        else:
            form = CitasForm(instance=cita)
        return render(request, 'veterinariaapp/citas_edit.html', {'form': form ,'cita':cita,'usuarios':usuarios})
    else :
        return redirect('url_login')

#Eliminar una cita
def citas_delete(request, pk):
    if "session_usuario" in request.session:
        try:
            cita = Citas.objects.filter(id_cita=pk)
            cita.delete()
            messages.success(request, 'La cita se eliminó Correctamente')
            return redirect('url_citas_list')
        except:
            print("Error...")
            messages.error(request, 'La cita que quiere eliminar tiene dependencias asociadas')
            return redirect('url_citas_list')
    else :
        return redirect('url_login')