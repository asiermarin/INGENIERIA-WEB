from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstView, name='FirstView'),
    path('articulo/<int:id>', views.OtherView, name='OtherView'),
    path('index', views.index, name='index'),
]