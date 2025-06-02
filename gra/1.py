import pygame

from gra.gracz import Gracz
from gra.wrog import Wrog

pygame.init()

# Ustawienia okna gry
okno = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Rzeźnia')

# Ładowanie tła
wstep = pygame.image.load('skorki/wstep.png')
okno_gry = pygame.image.load('skorki/zamek2.jpg')

# Licznik klatek
clock = pygame.time.Clock()
FPS = 60

# === Tworzenie obiektów ===
gracz = Gracz(100, 300, 'skorki/1.bmp')
wrog = Wrog(1000, 300, 'skorki/w.png')

# === Flagi gry ===
gra = True
wstep_aktywny = True
game_over = False

while gra:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gra = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                gracz.ruchY += 2
            if event.key == pygame.K_UP:
                gracz.ruchY -= 2
            if event.key == pygame.K_RIGHT:
                gracz.ruchX += 2
            if event.key == pygame.K_LEFT:
                gracz.ruchX -= 2

    klawisze = pygame.key.get_pressed()

    if wstep_aktywny:
        okno.blit(wstep, (0, 0))
        if klawisze[pygame.K_SPACE]:
            wstep_aktywny = False
    elif game_over:
        okno.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 80)
        tekst = font.render("Przegrałeś!", True, (255, 0, 0))
        okno.blit(tekst, (450, 350))
    else:
        okno.blit(okno_gry, (0, 0))
        gracz.sterowanie(klawisze)
        gracz.rysuj(okno)
        wrog.rysuj(okno)

        # Kolizje
        if gracz.get_rect().colliderect(wrog.get_rect()):
            game_over = True  # lub np. gracz.hp -= 1

    pygame.display.update()
