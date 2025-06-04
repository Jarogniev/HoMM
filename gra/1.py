import pygame
import random

from gra.gracz import Gracz
from gra.wrog import Wrog



def stworz_wrogow():
    wrogowie = []
    for _ in range(4):
        x = 1150  # prawy skraj planszy
        y = random.randint(50, 700)
        wrogowie.append(Wrog(x, y, 'skorki/w.png'))
    return wrogowie

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
wrogowie = stworz_wrogow()

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
            if event.key == pygame.K_SPACE:
                gracz.atakuj()

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
        gracz.aktualizuj_atak()
        gracz.sterowanie(klawisze)
        gracz.rysuj(okno)
        for wrog in wrogowie:
            if wrog.hp > 0:
                wrog.rysuj(okno)
        if gracz.hp <= 0:
            game_over = True


        for wr in wrogowie:
            if wr.hp > 0 and gracz.get_rect().colliderect(wr.get_rect()):
                gracz.otrzymaj_obrazenia(1)
                print("Gracz oberwał od wroga!")
                gracz.x -= 20

        if gracz.atakuje:
            atak_rect = gracz.get_atak_rect()
            for wrog in wrogowie:
                if wrog.hp > 0 and atak_rect.colliderect(wrog.get_rect()):
                    wrog.otrzymaj_obrazenia(1)
                    print("Jeb z dzidy laserowej!")


        okno.blit(okno_gry, (0, 0))
        gracz.sterowanie(klawisze)
        gracz.rysuj(okno)
        for rys in wrogowie:
            rys.rysuj(okno)


    pygame.display.update()
