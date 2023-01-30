import pygame
pygame.init()

ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejercicio 1")

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

ventana.fill((255, 255, 255))
pygame.display.flip()
pygame.time.Clock().tick(60)