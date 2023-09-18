from django.contrib import admin
from .models import Proveedor, Direccion, Cliente, Categoria, Producto, Venta, DetalleVenta

admin.site.register(Proveedor)
admin.site.register(Direccion)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
