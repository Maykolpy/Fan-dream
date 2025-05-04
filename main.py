import pygame
import sys

pygame.init()

pantalla = pygame.display.set_mode((400, 250))
pygame.display.set_caption("Fan dream")

try:
    pepe = pygame.image.load("sprites/pepep.png")
    pepe1 = pygame.image.load("sprites/pepe.png")
    pepe2 = pygame.image.load("sprites/pepepp.png")
except pygame.error as e:
    print("Error cargando una imagen:", e)
    pygame.quit()
    sys.exit()

scale_factor = 8
pepe2 = pygame.transform.scale(
    pepe2,
    (pepe2.get_width() * scale_factor, pepe2.get_height() * scale_factor)
)

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    pantalla.fill((0, 0, 0))
    pantalla.blit(pepe, (150, 100))
    pantalla.blit(pepe1, (150, 150))
    pantalla.blit(pepe2, (150, 200))  # Aquí cambié para que muestre pepe2 escalado

    pygame.display.update()

pygame.quit()