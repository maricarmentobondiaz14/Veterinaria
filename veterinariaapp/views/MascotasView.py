#importar modelos
from veterinariaapp.models.Mascotas import Mascotas
from veterinariaapp.models.Usuarios import Usuarios
from django.shortcuts import render, redirect, get_object_or_404

# importar formulario
from veterinariaapp.forms.MascotasForm import MascotasForm
from django.contrib import messages


#Obtener mascotas
def mascotas_list(request):
    if "session_usuario" in request.session:
        usuarios = Usuarios.objects.all().order_by('usuario')
        us = request.session['session_usuario']
        mascotas = Mascotas.objects.all().filter(usuario=us).order_by('nombre')


        if request.POST.get('nombre'):
            nombre = request.POST.get('nombre')
            mascotas = Mascotas.filter(nombre__icontains=nombre)
        else:
             nombre = None
        return render(request, 'veterinariaapp/mascotas_list.html', {'usuarios': usuarios,
                                                                     'mascotas': mascotas,
                                                                     'nombre': nombre
                                                                    })
    else :
        return redirect('url_login')


#Agregar una mascota
def mascotas_new(request):
    if "session_usuario" in request.session:
        messages.info(request, 'Nueva Mascota')
        usuarios = Usuarios.objects.all().order_by('usuario')
        us = request.session['session_usuario']

        form = MascotasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_mascotas_list')
        else:
            form = MascotasForm()
            print(form)

            return render(request, 'veterinariaapp/mascotas_edit.html', {'form': form,'usuarios':usuarios,'us':us})
    else :
        return redirect('url_login')

#Editar una linea
def mascotas_edit(request, pk):
    if "session_usuario" in request.session:
        messages.info(request, 'Editar Mascotas')
        us = request.session['session_usuario']
        usuarios = Usuarios.objects.all().order_by('usuario')
        mascota = get_object_or_404(Mascotas, pk=pk)
        if request.method == "POST":
            form = MascotasForm(request.POST, instance=mascota)
            if form.is_valid():
                print(form)
                form.save()
                return redirect('url_mascotas_list')
        else:
            form = MascotasForm(instance=mascota)
            print(form)

        return render(request, 'veterinariaapp/mascotas_edit.html', {'form': form ,'mascota':mascota,'usuarios':usuarios,'us':us})
    else :
        return redirect('url_login')

#Eliminar linea
def mascotas_delete(request, pk):
    if "session_usuario" in request.session:
        try:
            mascota = Mascotas.objects.filter(id_mascota=pk)
            mascota.delete()
            messages.success(request, 'La mascota se eliminó Correctamente')
            return redirect('url_mascotas_list')
        except:
            print("Error...")
            messages.error(request, 'La mascota que quiere eliminar tiene dependencias asociadas')
            return redirect('url_mascotas_list')
    else :
        return redirect('url_login')