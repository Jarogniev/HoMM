
import pygame


class Wrog:
    def __init__(self, x, y, obraz):
        self.x = x
        self.y = y
        self.obraz = pygame.image.load(obraz)
        self.szerokosc = self.obraz.get_width()
        self.wysokosc = self.obraz.get_height()
        self.hp = 2

    def rysuj(self, ekran):
        ekran.blit(self.obraz, (self.x, self.y))
        self.rysuj_hp(ekran)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)

    def otrzymaj_obrazenia(self, ilosc):
        self.hp -= ilosc
        if self.hp < 0:
            self.hp = 0

    def rysuj_hp(self, ekran):
        for i in range(self.hp):
            pygame.draw.rect(ekran, (255, 0, 0), (self.x + i * 15, self.y - 10, 10, 5))
