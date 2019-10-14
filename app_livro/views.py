from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LivroForm
from .services import livro_services
from .entidade.livro import Livro

@login_required
def listar_livros(request):
    livros = livro_services.listar_livros()
    return render(request,'manipulacao_de_livros/livros.html', {"livros": livros})
@login_required
def cadastrar_livro(request):
    if request.method == "POST":
        form_livro = LivroForm(request.POST)
        if form_livro.is_valid():
            titulo = form_livro.cleaned_data['titulo']
            genero = form_livro.cleaned_data['genero']
            autor = form_livro.cleaned_data['autor']
            livro_novo = Livro(titulo=titulo, genero=genero, autor=autor)
            livro_services.cadastrar_livro(livro_novo)
            return redirect('listar_livros')
    else:
        form_livro = LivroForm()
        return render(request, 'manipulacao_de_livros/form_livro.html', {"form_livro": form_livro})

@login_required
def editar_livro(request, id):
    livro_bd =  livro_services.listar_livro_id(id)
    form_livro = LivroForm(request.POST or None, instance=livro_bd)
    if form_livro.is_valid():
        titulo = form_livro.cleaned_data["titulo"]
        genero = form_livro.cleaned_data["genero"]
        autor = form_livro.cleaned_data["autor"]
        livro_novo = Livro(titulo=titulo,genero=genero,autor=autor)
        livro_services.editar_livro(livro_bd, livro_novo)
        return redirect ('listar_livros')
    return render(request, 'manipulacao_de_livros/form_livro.html', {"form_livro": form_livro})
@login_required
def remover_livro(request, id):
    livro_bd = livro_services.listar_livro_id(id)
    if request.method == "POST":
        livro_services.remover_livro(livro_bd)
        return redirect('listar_livros')
    return render(request, 'manipulacao_de_livros/confirmar_exclusao.html', {'livro_bd': livro_bd})