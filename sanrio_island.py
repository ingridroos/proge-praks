# proge-praks

import pygame, random
pygame.init()

# ekraani seaded
screenX = 1500
screenY = 800
screen = pygame.display.set_mode([screenX, screenY])
running=True
pygame.display.set_caption("Sanrio Island")
clock = pygame.time.Clock()

#Tegelane Kitty
kitty_pilt=pygame.image.load('kitty.png')
kitty_pilt=pygame.transform.scale(kitty_pilt,(100,100))
kitty_liigub=pygame.image.load('kitty_walk.png')
kitty_liigub=pygame.transform.scale(kitty_liigub, (100,100))

#Tegelane Pochacco
pochacco_pilt=pygame.image.load('pochacco.png')
pochacco_pilt=pygame.transform.scale(pochacco_pilt, (100,100))
pochacco_liigub=pygame.image.load('pochacco_walk.png')
pochacco_liigub=pygame.transform.scale(pochacco_liigub, (100,100))

#Tegelane Kuromi
kuromi_pilt=pygame.image.load('kuromi.png')
kuromi_pilt=pygame.transform.scale(kuromi_pilt, (100,100))
kuromi_liigub=pygame.image.load('kuromi_walk.png')
kuromi_liigub=pygame.transform.scale(kuromi_liigub, (100,100))

#Alguskoordinadid
x=200
y=600
samm=5

pygame.key.set_repeat(1,10)
while running:
    # taustapilt
    '''taustapilt=pygame.image.load("pilt.png")
    pygame.mixer.init()'''

    for i in pygame.event.get():
        screen.fill([255, 255, 255])

        # Kuvan Kitty taustale (tuleks lõpuks teha nii, et tegelast saab valida)
        screen.blit(kitty_pilt, (x, y))

        #Mängu sulgemine ristist
        if i.type == pygame.QUIT:
            running = False
        # Kui sündmuseks on klahvi allavajutamine…
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP: #Kitty ei oska alla tagasi tulla :(
                screen.fill([255, 255, 255])
                y = y - samm
                screen.blit(kitty_liigub, (x, y))
            elif i.key == pygame.K_DOWN:
                screen.fill([255, 255, 255])
                screen.blit(kitty_liigub, (x, y))
            #Järgnevas peame tausta panema liikuma, mitte tegelase,
            # aga Grete pole pilti veel teinud mulle mida liigutada >:(
            '''elif i.key == pygame.K_LEFT:
                x = x - samm
            elif i.key == pygame.K_RIGHT:
                x = x + samm'''

        clock.tick(60)
        pygame.display.flip()

pygame.quit()
