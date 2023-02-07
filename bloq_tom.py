import pygame.image
class bloque:
    def __init__(self, pt_x, pt_y, imagen):
        """
        :param pt_x:punto horizontal/X de la ventana
        :param pt_y:punto vertical/Y del la ventana
        :param imagen: imagen del ladrillo entre ""
        """
        self.x = pt_x
        self.y = pt_y
        self.imagen = pygame.image.load(imagen)
        self.imagenrect = pygame.Rect(self.x, self.y)
