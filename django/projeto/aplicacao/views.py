from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Olá do Django!")

def outra_view(request):
    return HttpResponse("Bem vindo, essa é a outa view!")

# Create your views here.
