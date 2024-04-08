class Toyota:

    def __init__(self, color='red', price=1e6, max_speed=200, current_speed=0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def check_info(self):
        print(self.color, self.price, self.max_speed, self.current_speed)

    def change_speed(self, new_speed):
        self.current_speed = new_speed
auto_1 = Toyota('Punainen', 10 ** 6, 200, 0)
auto_1.check_info()
auto_1.change_speed(150)
auto_1.check_info()