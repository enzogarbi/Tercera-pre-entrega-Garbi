from django.urls import path
from .views import *
from . import views

urlpatterns = [

    path('', PaginaInicioView.as_view(), name='inicio'),
    path('registro/', PaginaRegistroView.as_view(), name='registro'),
    path('login/', PaginaLoginView.as_view(), name='login'),
    path('menu/', PaginaMenuView.as_view(), name='menu'),
    path('acciones_venta/', AccionesVentaView.as_view(), name='acciones_venta'),
    path('clientes/', PaginaClientesView.as_view(), name='clientes'),
    path('clientes/lista/', ClienteList.as_view(), name='cliente_list'),
    path('clientes/crear/', ClienteCreate.as_view(), name='cliente_create'),
    path('clientes/editar/<int:pk>/', ClienteEditView.as_view(), name='editar_cliente'),
    path('clientes/borrar/<int:pk>/', ClienteDeleteView.as_view(), name='borrar_cliente'),
    path('proveedores/borrar/<int:pk>/', ProveedorDeleteView.as_view(), name='borrar_proveedor'),
    path('proveedores/', PaginaProveedoresView.as_view(), name='proveedores'),
    path('proveedores/lista/', ProveedorList.as_view(), name='proveedor_list'),
    path('proveedores/crear/', ProveedorCreate.as_view(), name='proveedor_create'),
    path('proveedores/editar/<int:pk>/', ProveedorEditView.as_view(), name='proveedor_edit'),
    path('proveedores/borrar/<int:pk>/', ProveedorDeleteView.as_view(), name='proveedor_delete'),
    path('presupuestos/', PaginaPresupuestosView.as_view(), name='presupuestos'),
        path('ordenes_compra_list/', PaginaOrdenesCompraListView.as_view(), name='ordenes_compra_list'),
    path('subir_orden_compra/', subir_orden_compra, name='subir_orden_compra'),
    path('subir_orden_compra_exitosa/', SubirOrdenCompraExitosa.as_view(), name='subir_orden_compra_exitosa'),
    
   
]



