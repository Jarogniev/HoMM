
import pygame


class Gracz:
    def __init__(self, x, y, obraz):
        self.x = x
        self.y = y
        self.obraz = pygame.image.load(obraz)
        self.ruchX = 0
        self.ruchY = 0
        self.predkosc = 1
        self.hp = 4
        self.szerokosc = self.obraz.get_width()
        self.wysokosc = self.obraz.get_height()
        self.atakuje = False
        self.atak_timer = 0
        self.niesmiertelnosc_czas = 1000  # ms
        self.ostatnie_obrazenia_od = {}  # słownik: {id(wroga): timestamp}

    def rysuj(self, ekran):
        ekran.blit(self.obraz, (self.x, self.y))
        self.rysuj_hp(ekran)
        if self.atakuje:
            pygame.draw.rect(ekran, (255, 0, 0), self.get_atak_rect())

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

    def get_atak_rect(self):
        # Atak mieczem na prawo od gracza
        return pygame.Rect(self.x + self.szerokosc, self.y + 10, 20, self.wysokosc - 20)

    def atakuj(self):
        self.atakuje = True
        self.atak_timer = 10  # licznik klatek, jak długo trwa animacja ataku

    def aktualizuj_atak(self):
        if self.atakuje:
            self.atak_timer -= 1
            if self.atak_timer <= 0:
                self.atakuje = False

    def otrzymaj_obrazenia(self, ilosc, wrog_id):
        teraz = pygame.time.get_ticks()
        ostatni_czas = self.ostatnie_obrazenia_od.get(wrog_id, 0)

        if teraz - ostatni_czas < self.niesmiertelnosc_czas:
            return

        self.hp -= ilosc
        self.ostatnie_obrazenia_od[wrog_id] = teraz
        print(f"Gracz otrzymał obrażenia od wroga {wrog_id}! HP: {self.hp}")

    # def aktualizuj_niesmiertelnosc(self):
    #     teraz = pygame.time.get_ticks()
    #     if self.niesmiertelny and (teraz - self.czas_ostatniego_obrazenia >= self.czas_niesmiertelnosci):
    #         self.niesmiertelny = False

    def rysuj_hp(self, ekran):
        for i in range(self.hp):
            pygame.draw.rect(ekran, (0, 255, 0), (self.x + i * 15, self.y - 10, 10, 5))
