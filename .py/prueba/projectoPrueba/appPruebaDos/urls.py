from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstView, name='FirstView'),
    path('articulo/<int:articuloId>', views.DetailOfArticuloObject, name='artuculoDetailView'), # La variable articuloId es definida en el mñetodo de views.py
    path('index', views.Index, name='Index'),
    path('view', views.ViewObject.as_view()),
    path('detailView/<int:pk>', views.DetailViewObject.as_view(), name='detailView'),
    path('listView', views.ListViewObject.as_view(), name='listView'),
]