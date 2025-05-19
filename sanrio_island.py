# proge-praks

import pygame, random
pygame.init()
pygame.mixer.init()

# ekraani seaded
screenX = 1000
screenY = 144*1.5
screen = pygame.display.set_mode([screenX, screenY])
running=True
pygame.display.set_caption("Sanrio Island")
clock = pygame.time.Clock()

#Muusika
muusika1=pygame.mixer.Sound('muusika1.mp3')
muusika1.set_volume(0.6)
muusika1.play()

#Tegelane Kitty
kitty_pilt_flip=pygame.image.load('kitty.png')
kitty_pilt_flip=pygame.transform.scale(kitty_pilt_flip,(50,50))
kitty_pilt=pygame.transform.flip(kitty_pilt_flip,True,False)
kitty_liigub_flip=pygame.image.load('kitty_walk.png')
kitty_liigub_flip=pygame.transform.scale(kitty_liigub_flip, (50,50))
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

#Heli nupp
mängib=True
rect_x, rect_y, rect_width, rect_height = 10, 10, 100, 100
heli_on=pygame.image.load('on.png')
heli_on=pygame.transform.scale(heli_on, (100, 100))
heli_off=pygame.image.load('off.png')
heli_off=pygame.transform.scale(heli_off, (100, 100))

#Alguskoordinadid
x=200
y=100
samm=10
liigub=False

# taustapilt
piltx=0
pilty=0
pilt2x=1500
taustapilt=pygame.image.load("background.png")
taustapilt=pygame.transform.scale(taustapilt, (1500,144*1.5))
screen.blit(taustapilt, (piltx, pilty))

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
                if y>5: #et ta ülevalt ekraanilt välja ei saaks
                    y = y - samm

            elif i.key == pygame.K_DOWN:
                liigub=True

            elif i.key == pygame.K_LEFT:
                #if piltx==500 :
                piltx=piltx + samm

            elif i.key == pygame.K_RIGHT:
                piltx=piltx - samm
            screen.blit(taustapilt, (piltx, pilty))
            screen.blit(taustapilt, (pilt2x, pilty))
            screen.blit(kitty_liigub, (x, y))
            screen.blit(heli_on, (10, 10))

        elif i.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if(rect_x <= mouse_x <= rect_x + rect_width and rect_y <= mouse_y <= rect_y + rect_height):
                if mängib == True:
                    muusika1.set_volume(0)
                    mängib=False
                    screen.blit(heli_off, (10, 10))
                else:
                    muusika1.set_volume(0.6)
                    mängib=True
                    screen.blit(heli_on, (10, 10))


    if not pygame.event.get():
        if y < 140:
            y = y + 5
            screen.blit(taustapilt, (piltx, pilty))
            screen.blit(kitty_liigub, (x, y))
        if y == 140 and liigub==False:
            screen.blit(taustapilt, (piltx, pilty))
            screen.blit(kitty_pilt, (x, y))
        liigub = False

        clock.tick(60)
        pygame.display.flip()

pygame.quit()
