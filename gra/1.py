import pygame

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


# === Klasy ===
class Gracz:
    def __init__(self, x, y, obraz):
        self.x = x
        self.y = y
        self.obraz = pygame.image.load(obraz)
        self.ruchX = 0
        self.ruchY = 0
        self.predkosc = 1

    def rysuj(self, ekran):
        ekran.blit(self.obraz, (self.x, self.y))

    def sterowanie(self, klawisze):
        if klawisze[pygame.K_a]:
            self.x -= self.predkosc
        if klawisze[pygame.K_d]:
            self.x += self.predkosc
        if klawisze[pygame.K_w]:
            self.y -= self.predkosc
        if klawisze[pygame.K_s]:
            self.y += self.predkosc

        self.x += self.ruchX
        self.y += self.ruchY

        # Ograniczenia ekranu
        self.x = max(0, min(self.x, 1150))
        self.y = max(0, min(self.y, 760))


class Wrog:
    def __init__(self, x, y, obraz):
        self.x = x
        self.y = y
        self.obraz = pygame.image.load(obraz)

    def rysuj(self, ekran):
        ekran.blit(self.obraz, (self.x, self.y))


# === Tworzenie obiektów ===
gracz = Gracz(100, 300, 'skorki/1.bmp')
wrog = Wrog(1000, 300, 'skorki/w.png')

# === Flagi gry ===
gra = True
wstep_aktywny = True

# === Pętla gry ===
while gra:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gra = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                gracz.ruchY += 0.3
            if event.key == pygame.K_UP:
                gracz.ruchY -= 0.3
            if event.key == pygame.K_RIGHT:
                gracz.ruchX += 0.3
            if event.key == pygame.K_LEFT:
                gracz.ruchX -= 0.3

    klawisze = pygame.key.get_pressed()

    if wstep_aktywny:
        okno.blit(wstep, (0, 0))
        if klawisze[pygame.K_SPACE]:
            wstep_aktywny = False
    else:
        okno.blit(okno_gry, (0, 0))
        gracz.sterowanie(klawisze)
        gracz.rysuj(okno)
        wrog.rysuj(okno)

    pygame.display.update()
