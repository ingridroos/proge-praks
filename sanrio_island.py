# proge-praks

import pygame, random
pygame.init()

# ekraani seaded
screenX = 1200
screenY = 750
screen = pygame.display.set_mode([screenX, screenY])
running=True
pygame.display.set_caption("Sanrio Island")
clock = pygame.time.Clock()


#Tegelane Kitty
kitty_pilt_flip=pygame.image.load('kitty.png')
kitty_pilt_flip=pygame.transform.scale(kitty_pilt_flip,(100,100))
kitty_pilt=pygame.transform.flip(kitty_pilt_flip,True,False)
kitty_liigub_flip=pygame.image.load('kitty_walk.png')
kitty_liigub_flip=pygame.transform.scale(kitty_liigub_flip, (100,100))
kitty_liigub=pygame.transform.flip(kitty_liigub_flip,True,False)

#Tegelane Pochacco - flip puudu
pochacco_pilt=pygame.image.load('pochacco.png')
pochacco_pilt=pygame.transform.scale(pochacco_pilt, (100,100))
pochacco_liigub=pygame.image.load('pochacco_walk.png')
pochacco_liigub=pygame.transform.scale(pochacco_liigub, (100,100))

#Tegelane Kuromi - flip puudu
kuromi_pilt=pygame.image.load('kuromi.png')
kuromi_pilt=pygame.transform.scale(kuromi_pilt, (100,100))
kuromi_liigub=pygame.image.load('kuromi_walk.png')
kuromi_liigub=pygame.transform.scale(kuromi_liigub, (100,100))

#Alguskoordinadid
x=200
y=600
samm=10
liigub=False

# taustapilt
taustapilt=pygame.image.load("background.png")
screen.blit(taustapilt, (0, 0))

# Kuvan Kitty taustale (tuleks lõpuks teha nii, et tegelast saab valida)
screen.blit(kitty_pilt, (x, y))

# Et  liigutamiseks ei peaks pidevalt vajutama, kasutan klahvi allhoidmise kontrolli
pygame.key.set_repeat(1,10)
while running:
    for i in pygame.event.get():
        #Mängu sulgemine ristist
        if i.type == pygame.QUIT:
            running = False
        # Kui sündmuseks on klahvi allavajutamine…
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                y = y - samm
            elif i.key == pygame.K_DOWN:
                liigub=True
            screen.blit(taustapilt, (0, 0))
            screen.blit(kitty_liigub, (x, y))

    if not pygame.event.get():
        if y < 600:
            y = y + 5
            screen.blit(taustapilt, (0, 0))
            screen.blit(kitty_liigub, (x, y))
        if y == 600 and liigub==False:
            screen.blit(taustapilt, (0, 0))
            screen.blit(kitty_pilt, (x, y)



        clock.tick(60)
        pygame.display.flip()

pygame.quit()