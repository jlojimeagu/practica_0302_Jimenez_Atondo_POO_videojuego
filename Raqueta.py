import pygame
class Raqueta:
    def __init__(self, ventana):
        self.tamano = 80
        self.x = 600/2 - self.tamano/2
        self.y = 380
        self.centro = self.x + self.tamano/2
        self.ventana = ventana
        self.izq = False
        self.der = False

    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, self.tamano, 10))

    def mover(self):
        if self.izq: self.x -= 10
        if self.der: self.x += 10
        self.x = 0 if self.x < 0 else 600 - self.tamano if self.x + self.tamano > 600 else self.x
        self.centro = self.x + self.tamano / 2
