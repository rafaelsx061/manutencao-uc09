from django.shortcuts import render
from django.http import HttpResponse #importar o HttpResponse 

def saudacao(request):
    return HttpResponse("Olá do Django!")

def outra_view(request): #criei uma nova def que aparece "Bem vindo, essa é a outa view!"
    return HttpResponse("Bem vindo, essa é a outa view!")

# Create your views here.
