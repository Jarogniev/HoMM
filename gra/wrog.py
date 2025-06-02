
import pygame

class Wrog:
    def __init__(self, x, y, obraz):
        self.x = x
        self.y = y
        self.obraz = pygame.image.load(obraz)

    def rysuj(self, ekran):
        ekran.blit(self.obraz, (self.x, self.y))

