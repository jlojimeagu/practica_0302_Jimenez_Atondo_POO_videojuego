import pygame
class pelota:
    def __init__(self, ventana, x, y):
        self.ventana = ventana
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, 10, 10))

    def mover(self):
        self.x += self.vx
        self.y += self.vy