#importamos el path del proyecto
from django.urls import path
#importamos el view
from rest_luna.views import lista_producto, detalle_producto

from rest_luna.viewslogin import login
 
urlpatterns =[
    #lo agregamos al path
    path('lista_producto', lista_producto, name="lista_producto"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('login',login,name="login"),
]


