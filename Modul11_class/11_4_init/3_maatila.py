class Peruna:
    tila = ({0: 'Poissaoleva', 1: 'Itu', 2: 'Vihreä', 3: 'Kypsä'})

    def __init__(self, index):
        self.index = index
        self.tila = 0

    def kasvaa(self):
        if self.tila < 3:
            self.tila += 1
        self.tulosta_tila()

    def on_kyp(self):
        if self.tila == 3:
            return True
        return False

    def tulosta_tila(self):
        print('Nyt peruna {} on {}'.format(
            self.index, Peruna.tila[self.tila]
        ))

class Peruna_Peltto:

    def __init__(self, lasku):
        self.perunat = [Peruna(index) for index in range(1, lasku + 1)]

    def koko_kasvaa(self):
        print('Peruna kasvaa!')
        for i_peruna in self.perunat:
            i_peruna.kasvaa()

    def koko_on_kyp(self):
        if not all([i_peruna.on_kyp() for i_peruna in self.perunat]):
            print('Peruna ei ole kypsä!\n')
        else:
            print('Koko peruna ole kypsä. Voi kerätä')

minun_peltto = Peruna_Peltto(5)
minun_peltto.koko_on_kyp()
for _ in range(3):
    minun_peltto.koko_kasvaa()
    minun_peltto.koko_on_kyp()
