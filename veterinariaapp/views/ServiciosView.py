#importar modelos
from veterinariaapp.models.Servicios import Servicios

#importar forms
from veterinariaapp.forms.ServiciosForm import ServiciosForm

# paquetes y librerias
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import time


nombreServicio=None
def vw_servicios_list_general(request):
    vwServicios = Servicios.objects.all().order_by('nombre')
    return render(request,'veterinariaapp/servicios_list_general.html',{'vwServicios':vwServicios})


def vw_servicios_list(request):
    if "session_usuario" in request.session:
        us_tipousuario = request.session['session_tipousuario']
        if us_tipousuario==1:
            vwServicios = Servicios.objects.all().order_by('nombre')
            return render(request,'veterinariaapp/servicios_list.html',{'vwServicios':vwServicios})
        else:
            vwServicios = Servicios.objects.all().order_by('nombre')
            return render(request, 'veterinariaapp/servicios_list_cliente.html',
                          {'vwServicios': vwServicios})

    else:
        return redirect('url_login')


#Editar servicios
def vw_servicios_edit(request,pk):
    if "session_usuario" in request.session:
        messages.info(request, 'Editar Servicio')
        servicios_vw = get_object_or_404(Servicios, pk=pk)
        if request.method == "POST":
            form = ServiciosForm(request.POST, instance=servicios_vw)
            if form.is_valid():
                form.save()
                return redirect('url_servicios_list')
        else:
            form = ServiciosForm(instance=servicios_vw)
        return render(request, 'veterinariaapp/servicios_edit.html', {'form': form, 'servicios_vw': servicios_vw})
    else :
        return redirect('url_login')

#Agregar servicios
def vw_servicios_new(request):
    if "session_usuario" in request.session:
        messages.info(request, 'Nuevo Servicio')
        form = ServiciosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_servicios_list')
        else:
            form = ServiciosForm()
            return render(request, 'veterinariaapp/servicios_edit.html', {'form': form } )
    else :
        return redirect('url_login')

#Eliminar usuarios
def vw_servicios_delete(request,pk):
    if "session_usuario" in request.session:
        try:
            servicio = Servicios.objects.filter(id_servicio=pk)
            servicio.delete()
            messages.success(request, 'El servicio se eliminó Correctamente')
            return redirect('url_servicios_list')
        except:
            print("Error...")
            messages.error(request, 'El servicio que quiere eliminar tiene dependencias asociadas')
            return redirect('url_servicios_list')
    else :
        return redirect('url_login')
