from django.urls import path
from veterinariaapp.views.UsuariosView import *
from veterinariaapp.views.PrincipalView import *
from veterinariaapp.views.ServiciosView import *
from veterinariaapp.views.CitasView import *
from veterinariaapp.views.ProductosView import *
from veterinariaapp.views.MascotasView import *


urlpatterns = [
    path('usuarios/nuevo', vw_usuarios_new_general, name='url_usuarios_new_general'),
    path('administrador/usuarios/new', vw_usuarios_new, name='url_usuarios_new'),
    path('administrador/usuarios/', vw_usuarios_list, name='url_usuarios_list'),
    path('administrador/usuarios/<pk>/editar', vw_usuarios_edit, name='url_usuarios_edit'),
    path('administrador/usuarios/<pk>/eliminar', vw_usuarios_delete, name='url_usuarios_delete'),

    path('productos/',vw_productos_list,name='url_productos_list'),
    path('cliente/productos/', vw_productos_list_cliente, name='url_productos_list_cliente'),

    path('productos/<pk>/edit',vw_productos_edit,name='url_productos_edit'),
    path('productos/new',vw_productos_new,name='url_productos_new'),

    path('administrador/citas/', citas_list, name='url_citas_list'),
    path('cliente/citas/new', cita_new, name='url_citas_new'),

    path('administrador/citas/<pk>/eliminar', citas_delete, name='url_citas_delete'),

    path('servicios/', vw_servicios_list_general, name='url_servicios_list_general'),
    path('servicios/<pk>/delete', vw_servicios_delete, name='url_servicios_delete'),
    path('servicios/new', vw_servicios_new, name='url_servicios_new'),
    path('servicios/<pk>/edit', vw_servicios_edit, name='url_servicios_edit'),
    path('usuario/servicios/', vw_servicios_list, name='url_servicios_list'),

    path('cliente/mascotas', mascotas_list, name='url_mascotas_list'),
    path('cliente/mascotas/new', mascotas_new, name='url_mascotas_new'),
    path('cliente/mascotas/<pk>/edit', mascotas_edit, name='url_mascotas_edit'),
    path('cliente/mascotas/<pk>/eliminar', mascotas_delete, name='url_mascotas_delete'),

    path('consejos/mascotas',vw_mascotas,name='url_mascotas_consejos'),
    path('login/', vw_login, name='url_login'),
    path('cliente/', vw_inicioCliente, name='url_inicioCliente'),
    path('administrador/', vw_inicioAdministrador, name='url_inicioAdministrador'),

    path('salir/', vw_salir, name='url_salir'),

    path('', vw_inicio, name='url_inicio')


]
