from ..models import Livro

def cadastrar_livro(livro):
    Livro.objects.create(titulo=livro.titulo, genero=livro.genero, autor=livro.autor)

def listar_livros():
    return Livro.objects.all()

def listar_livro_id(id):
    return Livro.objects.get(id=id)

def editar_livro(livro_bd, livro_novo):
    livro_bd.titulo = livro_novo.titulo
    livro_bd.genero = livro_novo.genero
    livro_bd.autor = livro_novo.autor
    livro_bd.save(force_update=True)

def remover_livro(livro_bd):
    livro_bd.delete()