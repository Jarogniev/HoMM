
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

    def podazaj_za_graczem(self, gracz):
        if self.hp <= 0:
            return

        if self.x > gracz.x:
            self.x -= 1
        elif self.x < gracz.x:
            self.x += 1

        if self.y > gracz.y:
            self.y -= 1
        elif self.y < gracz.y:
            self.y += 1
