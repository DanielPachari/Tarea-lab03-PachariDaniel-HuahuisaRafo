from django.db import models
from django.utils import timezone

class Proveedor(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    pagina_web = models.CharField(max_length=100)

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    comuna = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

class Cliente(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)
    telefonos = models.CharField(max_length=255)

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Producto(models.Model):
    identificador = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    def __str__(self):
        return f"Factura #{self.numero_factura}"

class Venta(models.Model):
    numero_factura = models.CharField(max_length=20, unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Factura #{self.numero_factura}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_vendida = models.PositiveIntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de Venta {self.venta.numero_factura} - {self.producto.nombre}"
