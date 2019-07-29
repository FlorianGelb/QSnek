from Main import MainWindow
import random
import time
from tkinter import *
from Snek import Snek
import numpy as np


class QSnekAI(MainWindow, Tk):
    def __init__(self):
        self.GAMMA = 0.4
        self.V = np.zeros((38,38))
        self.moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        super().__init__()

    def gen_e(self):
        chrs = ["w", "a", "s", "d"]
        return random.choice(chrs)

    def reward_in(self, x, y):

        if x == self.w.coords(self.apple)[0] / self.square_size - 2\
                and y == self.w.coords(self.apple)[1] / self.square_size -2:
            return 1000000

        for i in range(len(self.snek_array)):
            if ((x + 2) * self.square_size, (y + 2) * self.square_size) == self.snek_array[i].get_snek_pos():
                return -1

        if x == self.snek.get_snek_pos()[0] / self.square_size - 2  \
                and y == self.snek.get_snek_pos()[1] / self.square_size - 2:
            return -1

        if x > 38 or x < 0 or y > 38 or y < 0:
            return -1

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
                for i in range (len(self.moves)):
                    r =  self.reward_in(x, y)
                    v = self.getV(x + self.moves[i][0],y + self.moves[i][1])
                    if r != 0:
                        e = r + self.GAMMA * v
                    else:
                        e = self.GAMMA * v
                    if e != 0 :
                        e = round(e)

                        print("{} evald for X{} Y{}".format(e, x, y))
                        self.V[x][y] = e

    def create_label(self):
        self.labels = []
        for x in range(int(self.WIDTH)):
            for y in range(int(self.HEIGHT)):
                if x % self.square_size == 0 and y % self.square_size == 0:
                    self.l = self.w.create_text(x + 0.5 * self.square_size, y + 0.5 * self.square_size, text=str(self.getV(int(x / self.square_size - 2), int(y / self.square_size - 2))))
                    self.labels.append(self.l)

    def update_label(self, n, e):
        x = divmod(n, 38)[1]
        y = divmod(n, 38)[0]

        self.w.itemconfig(self.labels[n], text=str(self.getV(x,y)))

    def move(self, e):
        v2 = -10
        n = -10
        for x in range(len(self.moves)):
            v = self.getV(int((self.snek.get_snek_pos()[0] + self.moves[x][0] * 20) / self.square_size - 2), int((self.snek.get_snek_pos()[1] + self.moves[x][1] * 20) / self.square_size - 2))

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

        #if v == 0:
            #e = random.choice(["w", "a", "s", "d"])
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
            self.eval()
            self.update()
            time.sleep(0.0001)


    def loss(self):
        self.snek.set_snek_pos(19, 19)
        self.snek.set_snek_vector(0, 0)
        self.apple_cnt = 0

        for i in range(len(self.snek_array)):
            self.snek_array[0].snek_destroyer()
            del self.snek_array[0]

        #label = Label(0,0,self.w, self.apple_cnt)
        #self.w.create_window(10, 10, window=label)
        self.V = 38 * [[0] * 38]

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
