
import pygame


class Wrog:
    def __init__(self, x, y, obraz):
        self.x = x
        self.y = y
        self.obraz = pygame.image.load(obraz)
        self.szerokosc = self.obraz.get_width()
        self.wysokosc = self.obraz.get_height()

    def rysuj(self, ekran):
        ekran.blit(self.obraz, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
