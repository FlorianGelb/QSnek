from tkinter import *
from tkinter import Tk
import time

class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.WIDTH = 800
        self.HEIGHT = 800

        self.square_size = 20

        '''create_square requires 4 coordinates for the corners of the square'''
        x = 1
        y = 1
        self.snek_x1 = x * self.square_size
        self.snek_x2 = self.snek_x1 + self.square_size
        self.snek_y1 = y * self.square_size
        self.snek_y2 = self.snek_y1 + self.square_size

        self.snek_move_x = 0
        self.snek_move_y = 0

        self.m = PanedWindow(master=self.master, orient=VERTICAL, height=self.WIDTH, width=self.HEIGHT, background="blue",
                             borderwidth=20)
        self.m.pack(expand=0)

        self.w = Canvas(self.m, width=1200, height=1000)
        self.w.pack()
        self.m.add(self.w)

        self.create_game()

    def create_game(self):
        self.create_board()
        self.create_snek()
        self.loop()

    def create_snek(self):
        self.snek = self.w.create_rectangle(self.snek_x1, self.snek_y1, self.snek_x2,
                                self.snek_y2, fill="black")

    def move(self, e):
        if e.char == "d" or e.char == " ":
            self.snek_move_x = 1 * self.square_size
            self.snek_move_y = 0
        if e.char == "a":
            self.snek_move_x = -1 * self.square_size
            self.snek_move_y = 0
        if e.char == "w":
            self.snek_move_y = -1 * self.square_size
            self.snek_move_x = 0
        if e.char == "s":
            self.snek_move_y = 1 * self.square_size
            self.snek_move_x = 0

    def check_loss(self):
        if self.w.coords(self.snek)[0] >= self.WIDTH or self.w.coords(self.snek)[0]<0 or self.w.coords(self.snek)[1] >= \
                self.WIDTH or self.w.coords(self.snek)[1] < 0:
            self.w.coords(self.snek, 0,0)

    def loop(self):
            #print("x: {}    y: {}".format(self.w.coords(self.snek)[0], self.w.coords(self.snek)[1]))
        while 1:
            self.bind("<KeyPress>", self.move)
            self.w.move(self.snek, self.snek_move_x, self.snek_move_y)
            self.check_loss()
            self.update()
            time.sleep(0.1)

    def create_board(self):
        for x in range(self.WIDTH):
            if x % self.square_size == 0:
                self.w.create_line(x,0,x,self.HEIGHT, fill="black", width=1)
        for y in range(self.HEIGHT):
            if y% self.square_size == 0:
                self.w.create_line(0,y,self.WIDTH, y, fill="black", width=1)





if __name__ == "__main__":
    Mw = MainWindow()

