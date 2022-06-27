from django.shortcuts import render, redirect
from django.template import loader
from .models import Producto
from .forms import ProductoForm

# Create your views here.

#definir nuestro home, que sera index


def index(request):
    
    return render(request, 'core/index.html')


def nosotros(request):
    
    return render(request, 'core/Nosotros.html')


def catalogo(request):
    
    return render(request, 'core/Catalogo.html')


def formulario(request):
    
    return render(request, 'core/Formulario.html')


def registros(request):
    #accediendo al objeto que contiene los datos de la base
    #el metodo all traera todos los productos que estan en la tabla
    productos = Producto.objects.all()
    #ahora crearemos una variable que le pase los datos de los productos al template
    datos = {
        'productos': productos
    }
    #ahora lo agregamos para que se envie el template
    return render(request, 'core/registros.html', datos)


def registros_new_producto(request):
    #el view sera el responsable de entregar el form al template
    datos = {
        'form': ProductoForm()
    }
    #verificamos que peticion sean post y rescatamos los datos
    if request.method == 'POST':
        #con request recuperamos los datos del formulario
        formulario = ProductoForm(request.POST)
        #y validamos el formulario
        if formulario.is_valid:
            #ahora guardamos en la base de datos
            formulario.save()
            #y mostramos un mensaje
            datos['mensaje'] = 'Datos guardados correctamente'
    return render(request, 'core/registros_new_producto.html', datos)

def registros_mod_producto(request, id):
    #el id es el identificador de la tabla productos
    #buscara los datos en la base de datos
    #buscamos por sku que llega como dato en la url
    producto = Producto.objects.get(sku=id)
    #ahora le entregamos los datos del producto al formulario
    datos = {
        'form': ProductoForm(instance=producto)
    }

    #verificamos que peticion sean post y rescatamos los datos
    if request.method== 'POST':
        #con request recuperamos los datos del formulario y
        #le agregaremos el id a modificar
        formulario = ProductoForm(data=request.POST, instance=producto)
        #y validamos el formulario
        if formulario.is_valid:
            #ahora guardamos en la base de datos
            formulario.save()
            #y mostramos un mensaje
            datos['mensaje'] = "Modificados correctamente"

    return render(request, 'core/registros_mod_producto.html', datos)


def registros_del_producto(request, id):
    #el id es el identificador de la tabla productos
    #buscara los datos en la base de datos
    producto = Producto.objects.get(sku=id)
    #eliminamos el producto del id buscado
    producto.delete()
    #ahora redirigimos a home con el listado
    return redirect(to="registros")



def tienda(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/tienda.html', datos)

#def tienda2(request):
#    productos = Producto.objects.all()
#    datos = {
#        'productos': productos
#    }
#    return render(request, 'core/tienda2.html', datos)

