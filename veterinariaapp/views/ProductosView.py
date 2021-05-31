#importar modelos
from veterinariaapp.models.Productos import Productos

#importar forms
from veterinariaapp.forms.ProductosForm import ProductosForm

# paquetes y librerias
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import time

referenciaProducto=None
def vw_productos_list(request):
    if "session_usuario" in request.session:
        vwProductos = Productos.objects.all().order_by('referencia')
        global referenciaProducto

        if request.POST.get('referencia'):
            referenciaProducto = request.POST.get('referencia')
            vwProductos = vwProductos.filter(referencia__icontains=referenciaProducto)
        else:
            referenciaProducto = None

        return render(request,'veterinariaapp/productos_list.html',{'vwProductos':vwProductos,'referenciaProducto':referenciaProducto})
    else:
        return redirect('url_login')

def vw_productos_list_cliente(request):
    vwProductos = Productos.objects.all().order_by('referencia')
    return render(request,'veterinariaapp/productos_list_general.html',{'vwProductos':vwProductos})


#Editar productos
def vw_productos_edit(request,pk):
    if "session_usuario" in request.session:
        messages.info(request, 'Editar Usuario')
        productos_vw = get_object_or_404(Productos, pk=pk)
        if request.method == "POST":
            form = ProductosForm(request.POST, instance=productos_vw)
            if form.is_valid():
                form.save()
                messages.success(request, 'El producto se edito correctamente')
                return redirect('url_productos_list')
        else:
            form = ProductosForm(instance=productos_vw)
        return render(request, 'veterinariaapp/productos_edit.html', {'form': form, 'productos_vw': productos_vw})
    else :
        return redirect('url_login')

#Agregar productos
def vw_productos_new(request):
    if "session_usuario" in request.session:
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El producto se agregó correctamente')
            return redirect('url_productos_list')
        else:
            form = ProductosForm()
            return render(request, 'veterinariaapp/productos_edit.html', {'form': form } )
    else :
        return redirect('url_login')

#Eliminar usuarios
def vw_productos_delete(request,pk):
    if "session_usuario" in request.session:
        try:
            producto = Productos.objects.filter(id_producto=pk)
            producto.delete()
            messages.success(request, 'El producto se eliminó Correctamente')
            return redirect('url_productos_list')
        except:
            print("Error...")
            messages.error(request, 'El producto que quiere eliminar tiene dependencias asociadas')
            return redirect('url_productos_list')
    else :
        return redirect('url_login')