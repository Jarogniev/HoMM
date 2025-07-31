
import pygame


class Wrog:
    def __init__(self, x, y, obraz):
        self.x = x
        self.y = y
        self.obraz = pygame.image.load(obraz)
        self.szerokosc = self.obraz.get_width()
        self.wysokosc = self.obraz.get_height()
        self.hp = 2
        self.czas_ostatniego_ataku = 0  # w ms
        self.odstep_ataku = 1000  # 1000 ms
        self.obraz_normalny = pygame.image.load('skorki/gnoll.png').convert_alpha()
        self.obraz_po_trafieniu = pygame.image.load('skorki/martwy gnoll.bmp').convert_alpha()
        self.obraz = self.obraz_normalny
        self.trafiony = False
        self.czas_trafienia = 0
        self.czas_po_trafieniu = 5000  # 5 sekund

    def rysuj(self, okno):
        if self.hp > 0 or self.trafiony:
            okno.blit(self.obraz, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)

    def otrzymaj_obrazenia(self, ilosc):
        self.hp -= ilosc
        if self.hp <= 0 and not self.trafiony:
            self.trafiony = True
            self.czas_trafienia = pygame.time.get_ticks()
            self.obraz = self.obraz_po_trafieniu
            print("Wróg zdzidowany!")

    def aktualizuj_stan(self):
        if self.trafiony:
            teraz = pygame.time.get_ticks()
            if teraz - self.czas_trafienia >= self.czas_po_trafieniu:
                self.hp = 0  # definitywnie martwy

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

    def atakuj_gracza(self, gracz):
        teraz = pygame.time.get_ticks()

        if self.hp <= 0:
            return
        if self.get_rect().colliderect(gracz.get_rect()):
            if teraz - self.czas_ostatniego_ataku >= self.odstep_ataku:
                gracz.otrzymaj_obrazenia(1, id(self))
                self.czas_ostatniego_ataku = teraz
                print("Wróg dziduje!")
