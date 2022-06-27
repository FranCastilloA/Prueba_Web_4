#desde rest framework importamos serializers
from rest_framework import serializers
#desde models de core, importamos la clase Producto
from core.models import Producto
 
 
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['sku','nombreProducto','precio','stock','descripcion','imagen','categoria',]