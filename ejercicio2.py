import pygame
from pygame import mixer

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("the tom´s game")
#Crear el objeto pelota, define su velocidad y su rectángulo
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [5, 5]
ball_speed = 1
ballrect.move_ip(320, 240)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()

# pongo los parametros para la musica
mixer.init()
theme_sound = mixer.music.load('musica.mp3')
theme_sound = mixer.music.set_volume(10)
theme_sound = mixer.music.play()

# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(240, 450)

# Definimos el tipo de letra de Game over
fuente = pygame.font.Font(None, 36)

#Inicia el juego
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.K_SPACE == pygame.QUIT:
            jugando = False
    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-7, 0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(7, 0)

    # Compruebo si hay colisión
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    # Aumento velocidad de la pelota
    ballrect = ballrect.move(speed[0]*ball_speed, speed[1]*ball_speed)

    # Mensaje de Game Over
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125, 125, 125))
        text2 = fuente.render("press space to finish", True, (125, 125, 125))
        text2rect = text2.get_rect()
        textorect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - textorect.width / 2
        texto_y = ventana.get_height() / 2 - textorect.height / 2
        text2_x = ventana.get_width() / 2.2 - textorect.width / 2
        text2_y = ventana.get_height() / 2.5 - textorect.height / 2.5
        ventana.blit(texto, [texto_x, texto_y])
        ventana.blit(text2, [text2_x, text2_y])
        pygame.time.delay(3000)
    else:
        #dibujo a jerry
        ventana.fill((0, 0, 0))
        ventana.blit(ball, ballrect)

        # Dibujo el bate
        ventana.blit(bate, baterect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
