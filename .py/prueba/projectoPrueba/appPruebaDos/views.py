from django.http import HttpResponse
from django.shortcuts import render
from .models import Articulo

# /appPruebaDos
def FirstView(request):
    listaArticulos = Articulo.objects.order_by('id')
    context = {'listaArticulos' : listaArticulos}
    # return render(request, 'FirstView.html', listaArticulos)
    return render(request, 'FirstView.html', context)

# Metodo para otra pagina para devolver un articulo
# /appPruebaDos/articulo/][numero]
def OtherView(request, id):
    articuloYaExistente = Articulo.objects.get(pk=id)
    return HttpResponse(articuloYaExistente)

#/appPruebaDos/index
def index(request):
    listaArticulos = Articulo.objects.order_by('id')
    nombreTitulo = 'titulo desde codigo'
    context = {'titulo' : nombreTitulo, 'listaArticulos' : listaArticulos}
    
    return render(request, 'index.html', context)
