from Main import MainWindow
import random
import time
from tkinter import *
from Snek import Snek

class QSnekAI(MainWindow, Tk):
    def __init__(self):
        self.GAMMA = 0.9
        self.V = 38 * [[0] * 38]
        super().__init__()

    def gen_e(self):
        chrs = ["w", "a", "s", "d"]
        return random.choice(chrs)

    def reward_in(self, x, y):

        if x == self.w.coords(self.apple)[0] / self.square_size - 2\
                and y == self.w.coords(self.apple)[1] / self.square_size -2:
            return 10

        for i in range(len(self.snek_array)):
            if ((x + 2) * self.square_size, (y + 2) * self.square_size) == self.snek_array[i].get_snek_pos():
                return -10

        if x == self.snek.get_snek_pos()[0] / self.square_size - 2  \
                and y == self.snek.get_snek_pos()[1] / self.square_size - 2:
            return -10

        if x > 38 or x < 0 or y > 38 or y < 0:
            return -10

        return 0

    def getV(self, x, y):
        try:
            return self.V[x][y]
        except IndexError:
            return 0

    def setV(self, x, y, val):
        self.V[x][y] = val

    def eval(self):
        for x in range(int(self.WIDTH / self.square_size - 2)):
            for y in range(int(self.HEIGHT / self.square_size - 2)):
                e = self.reward_in(x, y) + self.GAMMA * self.getV(x,y)
                if e != 0:
                    print("{} evald for X{} Y{}".format(e, x, y))
                self.setV(x, y, e)


    def update_label(self):
        for x in range(38):
            for y in range(38):
                self.w.create_text(38 * x, 38 * y , text=str(self.V[x][y]))

    def move(self, e):
        moves = [[20, 0], [-20, 0], [0, 20], [0, -20]]
        v2 = 0
        n = 0
        for x in range(len(moves)):
            v = self.getV(int(self.snek.get_snek_pos()[0] + moves[x][0]), int(self.snek.get_snek_pos()[1] + moves[x][1]))

            if v > v2:
                n = x
                v2 = v


        if n == 0:
            e = "a"
        if n == 1:
            e = "d"
        if n == 2:
            e = "w"
        if n == 3:
            e == "s"

        if v == 0:
            e = random.choice(["w", "a", "s", "d"])
        try:
            e = e.char()
        except Exception as ex:
            pass

        if len(self.snek_array) > 0:
            if self.snek.snek_move_x == 20 and e == "a":
                self.loss()
            elif self.snek.snek_move_x == -20 and e == "d":
                self.loss()
            elif self.snek.snek_move_y == -20 and e == "s":
                self.loss()
            elif self.snek.snek_move_y == 20 and e == "w":
                self.loss()
        self.snek.set_move_snek(e)

    def loop(self):
        while 1:
            self.move(self.gen_e())
            self.snek.snek_move()
            self.check_collide()
            self.add_snek_tale()
            self.update_snek_tale()
            self.check_loss()
            self.update()
            self.eval()
            time.sleep(0.1)

    def create_board(self):
        self.snek = Snek(19, 19, self.square_size, self.w)
        self.create_apple()

        for x in range(self.WIDTH):
            if x % self.square_size == 0:
                self.w.create_line(x, 0, x, self.HEIGHT, fill="black", width=1)
        for y in range(self.HEIGHT):
            if y % self.square_size == 0:
                self.w.create_line(0, y, self.WIDTH, y, fill="black", width=1)


if __name__ == '__main__':
    test = QSnekAI()
