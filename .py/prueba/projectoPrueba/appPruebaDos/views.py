from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Articulo
from django.views import View
from django.views.generic import DetailView, ListView

# /appPruebaDos
def FirstView(request):
    listaArticulos = Articulo.objects.order_by('id')
    context = {'listaArticulos' : listaArticulos}
    # return render(request, 'FirstView.html', listaArticulos)
    return render(request, 'FirstView.html', context)

#/appPruebaDos/index
def Index(request):
    listaArticulos = Articulo.objects.order_by('id')
    nombreTitulo = 'titulo desde codigo'
    context = {
        'titulo' : nombreTitulo, 
        'listaArticulos' : listaArticulos
    }
    
    return render(request, 'index.html', context)

# Metodo para otra pagina para devolver un articulo
# /appPruebaDos/articulo/][numero]
def DetailOfArticuloObject(request, articuloId):
    articuloYaExistente = Articulo.objects.get(pk = articuloId)
    nombreTitulo = 'titulo desde codigo'
    context = {
        'titulo' : nombreTitulo, 
        'articuloExistente' : articuloYaExistente
    } # La variable que se va a utilizar en html es articuloExistente

    return render(request, 'articulo.html', context)

# /appPruebaDos/view NOT WORKS
class ViewObject(View):

    _listaArticulos = Articulo.objects.order_by('id')
    _nombreTitulo = 'titulo desde codigo'

    def Get(self, request):
        context = {
            'titulo' : _nombreTitulo, 
            'listaArticulos' : _listaArticulos
            }

        return render(request, 'plantillaView.html', context)

    
# /appPruebaDos/detailView/<int:pk>
# Solo pasa el modelo que se ha especificado si solo tenemos las dos primeras lineas
class DetailViewObject(DetailView):
    model = Articulo 
    template_name = "plantillaDetailView.html" # varible fijado del tipo DetailView

    def get_context_data(self, **kwargs):
        all_context = super(DetailViewObject, self).get_context_data(**kwargs) # esta variable no es necesaria una fijada, quizás solo las de campo
        all_context["titulo"] = "Titulo para detalles articulo DetailView"
        return all_context

    def post(self, request, *args, **kwargs):
        form = Articulo(request.POST)
        if form.is_valid():
            form.save()        

        return redirect('index')
    
class ListViewObject(ListView):
    model = Articulo
    template_name = "plantillaListView.html"
    querysetAllArticles = Articulo.objects.order_by("nombre") #nombre de la variable que queramos
    context_object_name = "lista_articulos_ya_existentes"  #Si yo quiero ponerle un sombre especifico

    # Metodo para incluir el titulo de la pagina tambien
    def get_context_data(self, **kwargs):
        all_context = super(ListViewObject, self).get_context_data(**kwargs) # esta variable no es necesaria una fijada, quizás solo las de campo
        all_context["titulo"] = "Titulo para detalles articulo ListView"
        return all_context
   
