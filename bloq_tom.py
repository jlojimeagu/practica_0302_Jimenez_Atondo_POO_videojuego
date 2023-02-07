class bloque:
    def __init__(self, x, y, puntos):

        super().__init__()  # herencia de otra clase

    # inicialización de otros objetos

        self.image = pg.image.load(os.path.join('resources’, ‘images’, ‘[]')

        self.rect = self.image.get_rect(x=x, y=y)

    self.puntos = puntos

