from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views



urlpatterns = [

    path('', listar_livros, name='listar_livros'),
    path('cadastrar_livro/', cadastrar_livro, name='cadastrar_livro'),
    path('editar_livro/<int:id>', editar_livro, name='editar_livro'),
    path('remover_livro/<int:id>', remover_livro, name='remover_livro'),
    path('signup/', views.SignUp.as_view(), name='signup'),


]

