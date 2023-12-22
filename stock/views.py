from django.shortcuts import render
from stock.models import ropa,accesorios,anteojos
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def crear_ropa(request):
    if request.method == "POST" :
        nueva_ropa = ropa(
            nombre = request.POST["nombre"],
            prenda = request.POST["prenda"],
            descripcion = request.POST["descripcion"],
            talle = request.POST["talle"],
            cantidad_en_stock = request.POST["cantidad en stock"],
        )
        nueva_ropa.save()
        return render(request, "index.html")
    return render(request, "ropa_formulario.html")

@login_required(login_url="login")
def crear_accesorio(request):
    if request.method == "POST" :
        nuevo_accesorio = accesorios(
            nombre = request.POST["nombre"],
            tipo = request.POST["tipo"],
            descripcion = request.POST["descripcion"],
            talle = request.POST["talle"],
            cantidad_en_stock = request.POST["cantidad en stock"],
        )
        nuevo_accesorio.save()
        return render(request, "index.html")

    return render(request, "accesorio_formulario.html")

@login_required(login_url="login")
def crear_anteojos(request):
    if request.method == "POST" :
        nuevos_anteojos = anteojos(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            color = request.POST["color"],
            cantidad_en_stock = request.POST["cantidad en stock"]
        )
        nuevos_anteojos.save()
        return render(request, "index.html")
    return render(request, "anteojos_formulario.html")


    
def busqueda_en_bd(request):
    if request.GET.get("nombre", False):
        busqueda = request.GET["nombre"]
        lista_ropa = ropa.objects.filter(nombre__icontains=busqueda)
   


        return render(request, "busqueda_bd.html", {"lista_ropa": lista_ropa})

    return render(request , "busqueda_bd.html")


def busqueda_en_bd(request):
    if request.GET.get("nombre", False): 

        busqueda = request.GET["nombre"]
        lista_ropa = ropa.objects.filter(nombre__icontains=busqueda)


        
        return render(request, 'busqueda_bd.html', {'lista': lista_ropa})
    
    return render(request, 'busqueda_bd.html')


def comprar_producto(request):

    if request.method == "POST":
        busqueda = request.POST["nombre"]
        lista_ropa = ropa.objects.get(nombre=busqueda)
        cantidad_compra = int(request.POST["cantidad"])

        lista_ropa.cantidad_en_stock = lista_ropa.cantidad_en_stock - cantidad_compra
        lista_ropa.save()
        
        return render(request, 'comprar_producto.html', {'ropa': lista_ropa.nombre, 'cantidad_stock': lista_ropa.cantidad_en_stock})
    
    return render(request, 'comprar_producto.html')




