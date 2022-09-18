from turtle import Turtle


class Brick(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.pos_x = x
        self.pos_y = y
        self.goto(x, y)

