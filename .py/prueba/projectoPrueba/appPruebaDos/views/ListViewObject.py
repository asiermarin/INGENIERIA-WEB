from django.http import HttpResponse
from django.shortcuts import render
from .models import Articulo
from django.views import View
from django.views.generic import DetailView, ListView


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