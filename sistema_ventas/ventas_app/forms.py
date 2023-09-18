from django import forms
from .models import Proveedor, Cliente, DetalleVenta, Venta, Producto

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['codigo', 'nombre', 'direccion', 'telefono', 'pagina_web']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['codigo', 'nombre', 'direccion', 'telefonos']

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['venta', 'producto', 'cantidad_vendida', 'monto_total']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'descuento', 'monto_final']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio_actual', 'stock', 'proveedor', 'categoria']