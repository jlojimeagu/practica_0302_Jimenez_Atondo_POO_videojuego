import pygame
class Bloques:
    def __init__(self, ventana):
        self.ventana = ventana
        self.tablero = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def dibujar(self):
        for i in range(4):
            for j in range(10):
                if self.tablero[i][j] != 0:
                    if self.tablero[i][j] == 4:
                        color = (255, 255, 255)
                    elif self.tablero[i][j] == 3:
                        color = (55, 255, 255)
                    elif self.tablero[i][j] == 2:
                        color = (55, 55, 255)
                    elif self.tablero[i][j] == 1:
                        color = (255, 55, 255)
                    pygame.draw.rect(self.ventana, color, (j * 60, i * 10 + 35, 59, 9))
