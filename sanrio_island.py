import pygame, random, time, sys
pygame.init()
pygame.mixer.init()

# Ekraani seaded
pygame.display.set_icon(pygame.image.load('kitty.png'))
screenX, screenY = 1000, int(144 * 1.5)
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Sanrio Island")
clock = pygame.time.Clock()

# Muusika
muusika1 = pygame.mixer.Sound('muusika1.mp3')
muusika1.set_volume(0.6)
muusika1.play(-1)

# Heli nupp
heli_rect = pygame.Rect(10, 10, 40, 40)
heli_on = pygame.transform.scale(pygame.image.load('on.png'), (40, 40))
heli_off = pygame.transform.scale(pygame.image.load('off.png'), (40, 40))

# Taustapilt
taustapilt = pygame.transform.scale(pygame.image.load("background.png"), (1500, screenY))
taust_laius = taustapilt.get_width()

# Tegelaste pildid ja flipid
class Tegelane:
    def __init__(self, nimi, pilt_path, liigub_path, suurus):
        self.nimi = nimi
        pilt = pygame.image.load(pilt_path)
        self.pilt = pygame.transform.flip(pygame.transform.scale(pilt, suurus), True, False)
        liigub_pilt = pygame.image.load(liigub_path)
        self.liigub = pygame.transform.flip(pygame.transform.scale(liigub_pilt, suurus), True, False)

tegelased = {
    "kitty": Tegelane("Kitty", 'kitty.png', 'kitty_walk.png', (50, 50)),
    "pochacco": Tegelane("Pochacco", 'pochacco.png', 'pochacco_walk.png', (50, 50)),
    "kuromi": Tegelane("Kuromi", 'kuromi.png', 'kuromi_walk.png', (50, 50))
}

mellow_pilt = pygame.transform.scale(pygame.image.load("mellow.png"), (50, 50))
squid_pilt = pygame.transform.scale(pygame.image.load("squid.png"), (50, 50))

font = pygame.font.SysFont(None, 36)

# Funktsioon mängu käivitamiseks
def run_game():
    mangib = True
    piltx = 0
    mellows = []
    squids = []
    skoor = 0
    mangu_algus = time.time()

    valitud_tegelane_nimi = random.choice(list(tegelased.keys()))
    valitud_tegelane = tegelased[valitud_tegelane_nimi]
    x, y = 200, 100
    samm = 10
    liigub = False

    next_mellow_time = time.time() + random.uniform(1, 3)
    next_squid_time = time.time() + random.uniform(2, 4)

    pygame.key.set_repeat(1, 10)
    running = True

    while running:
        aeg = time.time()
        if aeg - mangu_algus >= 60:
            return skoor

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP and y > 5:
                    y -= samm
                elif i.key == pygame.K_DOWN:
                    liigub = True
                elif i.key == pygame.K_LEFT:
                    piltx += samm
                elif i.key == pygame.K_RIGHT:
                    piltx -= samm
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if heli_rect.collidepoint(pygame.mouse.get_pos()):
                    mangib = not mangib
                    muusika1.set_volume(0.6 if mangib else 0)

        if aeg >= next_mellow_time:
            mellows.append(pygame.Rect(random.randint(100, screenX - 100), random.randint(50, screenY - 50), 50, 50))
            next_mellow_time = aeg + random.uniform(2, 4)

        if aeg >= next_squid_time:
            squids.append(pygame.Rect(random.randint(100, screenX - 100), random.randint(50, screenY - 50), 50, 50))
            next_squid_time = aeg + random.uniform(3, 5)

        tegelane_rect = pygame.Rect(x, y, 50, 50)

        for mellow in mellows[:]:
            if tegelane_rect.colliderect(mellow):
                mellows.remove(mellow)
                skoor += 1

        for squid in squids[:]:
            if tegelane_rect.colliderect(squid):
                squids.remove(squid)
                skoor -= 1

        for i in range(-1, (screenX // taust_laius) + 2):
            screen.blit(taustapilt, (piltx + i * taust_laius, 0))

        if y < screenY - 5:
            y = min(y + 5, screenY - 5)
            liigub = True

        screen.blit(valitud_tegelane.liigub if liigub else valitud_tegelane.pilt, (x, y))
        screen.blit(heli_on if mangib else heli_off, heli_rect.topleft)

        aeg_tekst = font.render(f"Aeg: {int(aeg - mangu_algus)}s", True, (0, 0, 0))
        skoor_tekst = font.render(f"Skoor: {skoor}", True, (0, 0, 0))
        screen.blit(skoor_tekst, (10, 60))
        screen.blit(aeg_tekst, (10, 100))

        for mellow in mellows:
            screen.blit(mellow_pilt, mellow.topleft)
        for squid in squids:
            screen.blit(squid_pilt, squid.topleft)

        liigub = False
        clock.tick(60)
        pygame.display.flip()

# Funktsioon lõppkuva ja restardi jaoks
def lopuekraan(skoor):
    while True:
        screen.fill((0, 0, 0))
        tekst = font.render(f"Mäng läbi! Lõppskoor: {skoor}", True, (255, 255, 255))
        restart = font.render("Vajuta R, et uuesti mängida või ESC, et väljuda", True, (200, 200, 200))
        screen.blit(tekst, (screenX // 2 - tekst.get_width() // 2, screenY // 2 - 40))
        screen.blit(restart, (screenX // 2 - restart.get_width() // 2, screenY // 2 + 10))
        pygame.display.flip()

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_r:
                    return True
                elif i.key == pygame.K_ESCAPE:
                    return False

# Mängu tsükkel koos restartiga
while True:
    skoor = run_game()
    if not lopuekraan(skoor):
        break

pygame.quit()
