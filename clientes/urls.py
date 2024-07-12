from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("clientes/", views.clientes, name="clientes"),
    path("cliente/<int:pk>", views.cliente_detalhe, name="cliente_detalhe"),
    path("cliente/<str:nome>", views.cliente_por_nome, name="cliente_por_nome"),
]
