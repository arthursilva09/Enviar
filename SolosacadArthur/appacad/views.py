from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'appacad/index.html')

def conteudo(request):
    return render(request, 'appacad/conteudo.html')

def prof(request, nome):
    return render(request, 'appacad/prof.html', {'nome':nome})

def aluno(request, nome):
    return render(request, 'appacad/aluno.html', {'nome': nome})

def login(request):
    return render(request, 'appacad/login.html')