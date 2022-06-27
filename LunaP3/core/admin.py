from django.contrib import admin
from .models import Categoria,Producto

# Register your models here.
#Para administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Producto)

#super user en maquina local de Pancho
#usuario: prueba3
#clave: prueba3Pancho
