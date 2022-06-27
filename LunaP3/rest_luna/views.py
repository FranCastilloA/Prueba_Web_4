#hay que importar lo basico primero
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
#importamos el modelo desde core y el serializer que creamos
from core.models import Producto
from .serializers import ProductoSerializer
# Agregamos lo siguiente que es para preparar el api local
@csrf_exempt
@api_view(['GET', 'POST'])
#ahora creamos nuestro codigo
def lista_producto(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#indicamos el apiview, de GET, PUT y DELETE
@api_view(['GET', 'PUT', 'DELETE'])
#funcion detalle producto  metodos GET, PUT y DELETE
def detalle_producto(request, id):
    try:
        #en este bloque try,  el id será el sku del producto
        # el cual lo busca en la base de datos, si existe lo asignaremos
        #a la variable v_producto
        v_producto = Producto.objects.get(sku=id)
    except Producto.DoesNotExist:
        #si no existe, devolveremos un 404
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(v_producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(v_producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        v_producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
