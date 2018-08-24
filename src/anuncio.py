class Anuncio():
    def __init__(self):
        self.precio = 0
        self.cuerpo = ""
        self.titulo = ""
        self.imagenes = []
        self.publicado = ""

    def __str__(self):
        return '{} ${}'.format(self.titulo, self.precio)

    