from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Olá Mundo")

def clientes(request):
    return HttpResponse("João, Maria, Pedro")

def cliente_detalhe(request, pk):
    return HttpResponse("Cliente detalhe %s" % pk)

def cliente_por_nome(request, nome):
    return HttpResponse("Olá %s" % nome)
