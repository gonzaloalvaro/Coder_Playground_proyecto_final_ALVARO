from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def pag_principal(request): 
    return render(request, "index.html")

def crear_ropa(request):
    return render(request, "ropa_formulario.html")

def crear_accesorio(request):
    return render(request, "accesorio_formulario.html")

def crear_anteojos(request):
    return render(request, "anteojos_formulario.html")

def busqueda_bd(request):
    return render(request, "busqueda_bd.html")

def buscar(request):
    respuesta = f"estoy buscando la prenda, accesorio o anteojo :  {request.GET['nombre']}" 


    