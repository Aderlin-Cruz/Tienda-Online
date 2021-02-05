from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Busqueda_Productos(request):
    
    
    return render (request, "busqueda_productos.html")


def buscar(request):
    
    mensaje="Artículo buscado: %r" %request.GET["prd"]

    return HttpResponse(mensaje)
