from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('livros/', listar_livros, name='listar_livros'),
    path('cadastrar_livro/', cadastrar_livro, name='cadastrar_livro'),
    path('editar_livro/<int:id>', editar_livro, name='editar_livro'),
    path('remover_livro/<int:id>', remover_livro, name='remover_livro'),
]