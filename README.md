# proge-praks

import pygame, random
pygame.init()

# ekraani seaded
screenX = 1500
screenY = 800
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Sanrio Island")
clock = pygame.time.Clock()

gameover=False
aeg=pygame.time.get_ticks()
while not gameover:
    # mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            gameover=True



clock.tick(60)

pygame.quit()
