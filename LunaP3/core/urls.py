from django.urls import path
from .views import index, nosotros, formulario, registros, tienda, registros_new_producto, registros_mod_producto, registros_del_producto

urlpatterns = [
    path('',index,name='index'),
    #path('',registros,name='registros'),
    path('index.html',index,name='index'),
    path('Nosotros.html',nosotros,name='nosotros'),
    path('Tienda.html',tienda,name='tienda'),
    path('Formulario.html',formulario,name='formulario'),
    path('registros.html',registros,name='registros'),
    path('registros_new_producto.html',registros_new_producto,name='registros_new_producto'),
    path('registros_mod_producto.html/<id>',registros_mod_producto,name='registros_mod_producto'),
    path('registros_del_producto/<id>', registros_del_producto, name="registros_del_producto"),
    #path('Tienda2.html',tienda2,name='tienda2'),
]
