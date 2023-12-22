from django.urls import path
from stock.views import crear_ropa, crear_accesorio,crear_anteojos,busqueda_en_bd,comprar_producto

urlpatterns = [
    path("crear_ropa/",crear_ropa, name= "crear_ropa" ),
    path("crear_accesorio/", crear_accesorio, name = "crear_accesorio"),
    path("crear_anteojos/",crear_anteojos, name = "crear_anteojos" ),
    path("busqueda_bd/", busqueda_en_bd, name = "busqueda en bd"),
    path('comprar_producto/', comprar_producto, name='comprar producto')
   
]