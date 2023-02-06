import pygame
#from pygame import mixer

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("the tom´s game")

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [5, 5]
ballrect.move_ip(320, 240)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()

# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(240, 450)

__bloque = pygame.image.load("ladrillo.png")
__ladrillo = __bloque.get_rect()
__ladrillo.move_ip(0, 0)
fuente = pygame.font.Font(None, 36)
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    keys = pygame.key.get_pressed()
    # Compruebo si se ha pulsado alguna tecla
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-7, 0)
    if keys[pygame.K_RIGHT]:

    # Compruebo si hay colisión
        baterect = baterect.move(7, 0)
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    # Mensaje de Game Over
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125, 125, 125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
        wait = pygame.time.wait(300)

    else:
        #dibujo a jerry
        ventana.fill((0, 0, 0))
        ventana.blit(ball, ballrect)
        # Dibujo el bate
        ventana.blit(bate, baterect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
