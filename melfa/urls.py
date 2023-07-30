from miapp.views import *
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miapp.urls')),
    path('login/', PaginaLoginView.as_view(), name='login'),
    path('registro/', PaginaRegistroView.as_view(), name='registro'),
    path('acciones_venta/', AccionesVentaView.as_view(), name='acciones_venta'),
    path('orden_de_compra/', PaginaOrdenesCompraView.as_view(), name='orden_de_compra'),
    path('ordenes_compra_list/', PaginaOrdenesCompraListView.as_view(), name='ordenes_compra_list'),
    
]

    


