from tkinter import *
import random
from Snek import *
import time


class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.WIDTH = 800
        self.HEIGHT = 800

        self.square_size = 20

        '''Canvas.create_rectangel takes 4 coords'''
        self.apple_x1 = 0
        self.apple_x2 = 0
        self.apple_y1 = 0
        self.apple_y2 = 0

        self.apple_cnt = 0
        self.old_apple_cnt = 0
        self.snek_array = []

        self.m = PanedWindow(master=self.master, orient=VERTICAL, height=self.WIDTH, width=self.HEIGHT, background="blue",
                             borderwidth=1)
        self.m.pack(expand=0)

        self.w = Canvas(self.m, width=1200, height=1000)
        self.w.pack()

        label = Label(self, text=str(self.apple_cnt))
        label.pack()
        self.w.create_window(10, 10, window=label)

        self.snek = None

        self.apple = None

        self.m.add(self.w)

        self.create_game()

    def create_game(self):
        self.create_board()
        self.loop()



    def create_apple(self):

        apple_x = random.randint(1, (self.WIDTH / self.square_size)-4)
        apple_y = random.randint(1, (self.HEIGHT / self.square_size)-4)

        self.apple_x1 = apple_x * self.square_size
        self.apple_x2 = self.apple_x1 + self.square_size
        self.apple_y1 = apple_y * self.square_size
        self.apple_y2 = self.apple_y1 + self.square_size

        self.apple = self.apple = self.w.create_rectangle(self.apple_x1, self.apple_y1, self.apple_x2,
                                self.apple_y2, fill="red")

    def move(self, e):
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

    def loss(self):
        self.snek.set_snek_pos(19, 19)
        self.snek.set_snek_vector(0, 0)
        self.apple_cnt = 0

        for i in range(len(self.snek_array)):
            self.snek_array[0].snek_destroyer()
            del self.snek_array[0]

        label = Label(self, text=str(self.apple_cnt))
        label.pack()
        self.w.create_window(10, 10, window=label)



    def check_loss(self):
        '''Collision with left und upper bound'''
        if self.snek.get_snek_pos()[0] < 0 or self.snek.get_snek_pos()[1] < 0:
            self.loss()
        '''Collision with right and lower bound'''
        if self.snek.get_snek_pos()[0] > self.WIDTH or self.snek.get_snek_pos()[1] > self.HEIGHT:
            self.loss()

        for i in range(len(self.snek_array) -1):
            if self.snek.get_snek_pos()[0] == self.snek_array[i].get_snek_pos()[0] \
                    and self.snek.get_snek_pos()[1] == self.snek_array[i].get_snek_pos()[1]:
                self.loss()


    def check_collide(self):
        if self.w.coords(self.apple) == self.snek.get_snek_pos():
            self.old_apple_cnt = self.apple_cnt
            self.apple_cnt += 1
            self.w.itemconfig(self.apple, fill="black")
            self.w.delete(self.apple)
            self.create_apple()

    def add_snek_tale(self):

        snek_tale = Snek((self.snek.get_snek_pos()[0] - self.snek.get_snek_move()[0]) / self.square_size + 1, \
                          (self.snek.get_snek_pos()[1] - self.snek.get_snek_move()[1]) / self.square_size + 1,\
                          self.square_size, self.w)
        self.snek_array.append(snek_tale)



    def update_label(self):
        if self.old_apple_cnt != self.apple_cnt:
            label = Label(self, text=str(self.apple_cnt))
            label.pack()
            self.w.create_window(10, 10, window=label)

    def update_snek_tale(self):
        if len(self.snek_array) > self.apple_cnt:
            self.snek_array[0].snek_destroyer()
            del self.snek_array[0]

    def loop(self):
        while 1:
            self.bind("<KeyPress>", self.move)
            self.snek.snek_move()
            self.check_collide()
            self.update_label()
            self.add_snek_tale()
            self.update_snek_tale()
            self.check_loss()
            self.update()
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




if __name__ == "__main__":
    Mw = MainWindow()
