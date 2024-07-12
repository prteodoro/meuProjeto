from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    sexo = "m"
    nome = "Pedro"
    lista = [
        {"nome": "Pedro", "sexo": "m"},
        {"nome": "Maria", "sexo": "f"},
        {"nome": "Joaquina", "sexo": "F"},
        {"nome": "Joao", "sexo": "M"}
    ]
    data = {"sexo": sexo, "nome": nome, "lista": lista}
    return render(request, "index.html", data)

def index(request):
    return HttpResponse("Olá Mundo")

def clientes(request):
    return HttpResponse("João, Maria, Pedro")

def cliente_detalhe(request, pk):
    return HttpResponse("Cliente detalhe %s" % pk)

def cliente_por_nome(request, nome):
    return HttpResponse("Olá %s" % nome)
