class Livro():
    def __init__ (self,titulo,genero,autor):
        self._titulo = titulo
        self._genero = genero
        self._autor = autor

    @property
    def titulo(self):
        return self._titulo

    @property
    def genero(self):
        return self._genero

    @property
    def autor(self):
        return self._autor

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @genero.setter
    def genero(self,genero):
        self._genero = genero

    @autor.setter
    def autor(self, autor):
        self._autor = autor