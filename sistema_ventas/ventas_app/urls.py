from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('', views.pagina_principal, name='pagina_principal'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('detalle_venta/agregar/', views.agregar_detalle_venta, name='agregar_detalle_venta'),
    path('agregar_venta/', views.agregar_venta, name='agregar_venta'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
]
