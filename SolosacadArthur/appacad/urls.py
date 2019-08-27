from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('conteudo/', views.conteudo),
    path('professor/<str:nome>', views.prof),
    path('aluno/<str:nome>', views.aluno),
    path('login/', views.login),

]