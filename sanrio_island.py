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

# Et  liigutamiseks ei peaks pidevalt vajutama, kasutan klahvi allhoidmise kontrolli
pygame.key.set_repeat(1,10)
while running:
    # taustapilt
    taustapilt=pygame.image.load("background.png")


    for i in pygame.event.get():
        screen.blit(taustapilt,(0, 0))

        # Kuvan Kitty taustale (tuleks lõpuks teha nii, et tegelast saab valida)
        screen.blit(kitty_pilt, (x, y))

        #Mängu sulgemine ristist
        if i.type == pygame.QUIT:
            running = False
        # Kui sündmuseks on klahvi allavajutamine…
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP: #Kitty ei oska alla tagasi tulla :(
                screen.blit(taustapilt,(0, 0))
                y = y - samm
                screen.blit(kitty_liigub, (x, y))
            elif i.key == pygame.K_DOWN:
                screen.blit(taustapilt,(0, 0))
                screen.blit(kitty_liigub, (x, y))

    if not pygame.event.get():
        if y <= 600:
            y = y + 5
        screen.fill([255, 255, 255])
        screen.blit(kitty_pilt, (x, y))


        clock.tick(60)
        pygame.display.flip()

pygame.quit()