
class Piste:
    count = 0

    def __init__(self, x, y):
        self.x_coor = x
        self.y_coor = y
        Piste.count += 1

    def tieto(self):
        print(self.x_coor, self.y_coor)

piste_1 = Piste(1,1)
piste_1.tieto()
print(piste_1.count)