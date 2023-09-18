from django.shortcuts import render, redirect
from .models import Proveedor, Cliente, Venta
from .forms import ProveedorForm, ClienteForm, DetalleVentaForm, VentaForm, ProductoForm
from django.utils import timezone

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores') 
    else:
        form = ProveedorForm()
    
    return render(request, 'agregar_proveedor.html', {'form': form})

def pagina_principal(request):
    return render(request, 'pagina_principal.html')

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'agregar_cliente.html', {'form': form})

def agregar_detalle_venta(request):
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas') 
    else:
        form = DetalleVentaForm()
    
    return render(request, 'agregar_detalle_venta.html', {'form': form})

def agregar_venta(request):
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            nueva_venta = venta_form.save(commit=False)
            nueva_venta.fecha = timezone.now()  
            nueva_venta.save()
            return redirect('ventas') 

    else:
        venta_form = VentaForm()

    return render(request, 'agregar_venta.html', {'venta_form': venta_form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos') 
    else:
        form = ProductoForm()
    
    return render(request, 'agregar_producto.html', {'form': form})