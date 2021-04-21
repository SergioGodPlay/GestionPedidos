from django.shortcuts import render
from .carro import Carro
from Tienda.models import Producto
from django.shortcuts import redirect


# Create your views here.

def agregarProducto(request, producto_id):

    carro = Carro(request)

    producto = Producto.objects.get(id = producto_id)

    carro.agregar(producto)

    return redirect("tienda")


def eliminarProducto(request, producto_id):

    carro = Carro(request)

    producto = Producto.objects.get(id = producto_id)

    carro.eliminar(producto)

    return redirect("tienda")


def restarProducto(request, producto_id):

    carro = Carro(request)

    producto = Producto.objects.get(id = producto_id)

    carro.restar_producto(producto)

    return redirect("tienda")


def limpiarCarro(request, producto_id):

    carro = Carro(request)

    carro.limpiar_carro()
    
    return redirect("tienda")

