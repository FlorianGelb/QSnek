class Label:
    def __init__(self, x, y, w, t):
        self.w = w
        self.x = x
        self.y = y
        self.t = t
        self.create_label()

    def create_label(self):
        self.label = self.w.create_text(self.x, self.y, text=self.t)

    def destroy_label(self):
        self.w.delete(self.label)
