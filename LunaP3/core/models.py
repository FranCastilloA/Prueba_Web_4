from django.db import models

# Create your models here.

#Modelo base datos

#modelo para Categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

#Modelo para Producto

class Producto(models.Model):

    sku = models.IntegerField(primary_key=True, verbose_name='SKU')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre de Producto')
    precio = models.IntegerField(null=False, blank=False, verbose_name='Precio Producto')
    stock = models.IntegerField(null=False, blank=False,verbose_name='Stock Producto')
    descripcion = models.CharField(max_length=250, verbose_name='Descripcion Producto')
    imagen = models.CharField(null=True, blank=True, max_length=1000, verbose_name='Url Imagen Producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProducto

        

