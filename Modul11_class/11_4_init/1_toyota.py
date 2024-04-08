import random


class Toyota:

    def __init__(self, color, hinta, h_nopeus, n_nopeus):
        self.v_clor = color
        self.hinta = hinta
        self.h_nopeus = h_nopeus
        self.n_nopeus = n_nopeus
    def tieto(self):
        print('Väri: {}\nHinta: {}\n Hiuppunopeus: {}\n Nykyinen nopeus: {}'.format(
            self.v_clor, self.hinta, self.h_nopeus, self.n_nopeus
        ))
    def nopeus_muuta(self):
        self.n_nopeus += random.randint(0, 200)


auto_1 = Toyota('Punainen', 10 ** 6, 200, 0)
auto_1.tieto()
auto_1.nopeus_muuta()
auto_1.tieto()

