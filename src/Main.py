from tkinter import *
from tkinter import Tk
import time
import random


class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.WIDTH = 800
        self.HEIGHT = 800

        self.square_size = 20

        self.snek = None
        self.apple = None

        '''create_square requires 4 coordinates for the corners of the square'''

        self.snek_x1 = 0
        self.snek_x2 = 0
        self.snek_y1 = 0
        self.snek_y2 = 0

        '''Same goes for the apple'''
        self.apple_x1 = 0
        self.apple_x2 = 0
        self.apple_y1 = 0
        self.apple_y2 = 0

        '''Vector for Snek'''
        self.snek_move_x = 0
        self.snek_move_y = 0

        self.snek_array = []

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
        self.create_apple()
        self.loop()

    def create_snek(self):

        snek_x = 1
        snek_y = 1

        self.snek_x1 = snek_x * self.square_size
        self.snek_x2 = self.snek_x1 + self.square_size
        self.snek_y1 = snek_y * self.square_size
        self.snek_y2 = self.snek_y1 + self.square_size

        self.snek = self.w.create_rectangle(self.snek_x1, self.snek_y1, self.snek_x2,
                                self.snek_y2, fill="black")
        self.snek_array.append(self.snek)

    def create_apple(self):

        apple_x = random.randint(0, (self.WIDTH / self.square_size)-2)
        apple_y = random.randint(0, (self.HEIGHT / self.square_size)-2)


        self.apple_x1 = apple_x * self.square_size
        self.apple_x2 = self.apple_x1 + self.square_size
        self.apple_y1 = apple_y * self.square_size
        self.apple_y2 = self.apple_y1 + self.square_size

        self.apple = self.apple = self.w.create_rectangle(self.apple_x1, self.apple_y1, self.apple_x2,
                                self.apple_y2, fill="red")

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

    def loss(self):
        self.w.coords(self.snek, 0, 0, self.square_size, self.square_size)
        self.snek_move_x = 0
        self.snek_move_y = 0

    def check_loss(self):
        if self.w.coords(self.snek)[0] >= self.WIDTH or self.w.coords(self.snek)[0]<0 or self.w.coords(self.snek)[1] >= \
                self.WIDTH or self.w.coords(self.snek)[1] < 0:
            self.loss()

    def check_collide(self):
        if self.w.coords(self.apple) == self.w.coords(self.snek):
            self.w.itemconfig(self.apple, fill="black")
            self.snek_array.append(self.apple)
            self.w.delete(self.apple)
            self.create_apple()
           # self.add_snek_tale()

    def add_snek_tale(self):

        if self.snek_move_x == 0 and self.snek_move_y == 1:

            x1 = self.w.coords(self.snek)[1] - self.square_size
            y1 = self.w.coords(self.snek)[3] - self.square_size

            x2 = self.w.coords(self.snek)[2] - self.square_size
            y2 = self.w.coords(self.snek)[3] - self.square_size

        self.w.create_rectangle(x1, y1, x2, y2, fill="black")
    def loop(self):
        self.w.coords(self.snek, 10,20, 10 ,20)
        print("x: {}    y: {}".format(self.w.coords(self.snek)[2], self.w.coords(self.snek)[3]))
        self.mainloop()
        #while 1:
        '''  self.bind("<KeyPress>", self.move)
            self.w.move(self.snek, self.snek_move_x, self.snek_move_y)
            self.check_loss()
            self.check_collide()
'''
           # self.update()
            #time.sleep(0.05)

    def create_board(self):
        for x in range(self.WIDTH):
            if x % self.square_size == 0:
                self.w.create_line(x,0,x,self.HEIGHT, fill="black", width=1)
        for y in range(self.HEIGHT):
            if y % self.square_size == 0:
                self.w.create_line(0,y,self.WIDTH, y, fill="black", width=1)


if __name__ == "__main__":
    Mw = MainWindow()
