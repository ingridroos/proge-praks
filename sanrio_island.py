# proge-praks

import pygame
import random
import sys
import time


pygame.init()
pygame.mixer.init()

font1 = pygame.font.SysFont('Arial', 40)

points = 0
start_time = time.time()



def show_menu():
    screen.fill([0, 0, 0])
    title = font1.render("Vajuta suvalist klahvi, et alustada", True, [255,255,255])
    screen.blit(title, (300, 72))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

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
mangib=True
rect_x, rect_y, rect_width, rect_height = 10, 10, 40, 40
heli_on=pygame.image.load('on.png')
heli_on=pygame.transform.scale(heli_on, (40, 40))
heli_off=pygame.image.load('off.png')
heli_off=pygame.transform.scale(heli_off, (40, 40))

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
taustapilt_flip=pygame.transform.flip(taustapilt,True,False)
screen.blit(taustapilt, (piltx, pilty))


# Kuvan Kitty taustale (tuleks lõpuks teha nii, et tegelast saab valida)
screen.blit(kitty_pilt, (x, y))

# Et  liigutamiseks ei peaks pidevalt vajutama, kasutan klahvi allhoidmise kontrolli
pygame.key.set_repeat(1,10)
show_menu()
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
            if mangib:
                screen.blit(heli_on, (10, 10))
            else:
                screen.blit(heli_off, (10, 10))


        elif i.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect_x <= mouse_x <= rect_x + rect_width and rect_y <= mouse_y <= rect_y + rect_height:
                if mangib:
                    muusika1.set_volume(0)
                    mangib=False
                    screen.blit(heli_off, (10, 10))
                else:
                    muusika1.set_volume(0.6)
                    mangib=True
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
        if mangib:
            screen.blit(heli_on, (10, 10))
        else:
            screen.blit(heli_off, (10, 10))



        elapsed_time = int(time.time() - start_time)
        point_text = font1.render(f"Punktid: {points}", True, [255, 255, 255])
        time_text = font1.render(f"Aeg: {elapsed_time}s", True, [255, 255, 255])
        screen.blit(point_text, (10, 60))
        screen.blit(time_text, (10, 100))

        clock.tick(60)
        pygame.display.flip()

pygame.quit()
