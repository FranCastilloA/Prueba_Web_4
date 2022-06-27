from django import forms
from django.forms import ModelForm
from .models import Producto

#creamos nuestra clase para el formulario desde la base de datos
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['sku','nombreProducto','precio','stock','descripcion','imagen','categoria',]



        