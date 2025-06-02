# cały gracz
import pygame


class Gracz:
    def __init__(self, x, y, obraz):
        self.x = x
        self.y = y
        self.obraz = pygame.image.load(obraz)
        self.ruchX = 0
        self.ruchY = 0
        self.predkosc = 1
        self.szerokosc = self.obraz.get_width()
        self.wysokosc = self.obraz.get_height()

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

        self.x = max(0, min(self.x, 1150))
        self.y = max(0, min(self.y, 760))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
