from Main import MainWindow
import random
import time


class TestClass(MainWindow):
    def __init__(self):
        super().__init__()

    def gen_e(self):
        chrs = ["w", "a", "s", "d"]
        return random.choice(chrs)

    def loop(self):
        while 1:
            self.move(self.gen_e())
            self.snek.snek_move()
            self.check_collide()
            self.update_label()
            self.add_snek_tale()
            self.update_snek_tale()
            self.check_loss()
            self.update()
            time.sleep(0.00001)

if __name__ == '__main__':
    test = TestClass()
