class Snek:

    def __init__(self, x, y, square_size, w):
        self.snek_x = x - 1
        self.snek_y = y - 1

        self.snek_move_y = 0
        self.snek_move_x = 0

        self.square_size = square_size

        self.w = w
        self.create_snek()

        self.last_vx = 0
        self.last_vy = 0

        self.last_x = self.get_snek_pos()[0]
        self.last_y = self.get_snek_pos()[1]

    def create_snek(self):

        self.snek_x1 = self.snek_x * self.square_size
        self.snek_x2 = self.snek_x1 + self.square_size
        self.snek_y1 = self.snek_y * self.square_size
        self.snek_y2 = self.snek_y1 + self.square_size

        self.snek = self.w.create_rectangle(self.snek_x1, self.snek_y1, self.snek_x2,
                                            self.snek_y2, fill="black")

    def set_move_snek(self, e):
        self.last_x = self.get_snek_pos()[0]
        self.last_y = self.get_snek_pos()[1]
        try:
            e = e.char
        except Exception as ex:
            pass


        if e == "d" or e == " ":
            self.snek_move_x = 1 * self.square_size
            self.snek_move_y = 0
        if e == "a":
            self.snek_move_x = -1 * self.square_size
            self.snek_move_y = 0
        if e == "w":
            self.snek_move_y = -1 * self.square_size
            self.snek_move_x = 0
        if e == "s":
            self.snek_move_y = 1 * self.square_size
            self.snek_move_x = 0




    def snek_move(self):
        self.last_vx = self.snek_move_x
        self.last_vy = self.snek_move_y
        self.w.move(self.snek, self.snek_move_x, self.snek_move_y)

    def get_snek_pos(self):
        return self.w.coords(self.snek)

    def set_snek_pos(self, new_x, new_y):
        new_snek_x1 = new_x * self.square_size
        new_snek_x2 = new_snek_x1 + self.square_size
        new_snek_y1 = new_y * self.square_size
        new_snek_y2 = new_snek_y1 + self.square_size
        self.w.coords(self.snek, new_snek_x1, new_snek_y1, new_snek_x2, new_snek_y2)

    def get_snek_move(self):
        return (self.snek_move_x, self.snek_move_y)

    def set_snek_vector(self, vx, vy):
        self.last_x = self.get_snek_pos()[0]
        self.last_y = self.get_snek_pos()[1]

        self.snek_move_x = vx
        self.snek_move_y = vy

    def snek_destroyer(self):
        self.w.delete(self.snek)