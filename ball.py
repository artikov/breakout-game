import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = -10
        self.y_move = -10
        self.setheading(random.randint(1, 179))
        self.goto(-50, -210)

    def reset_position(self):
        self.goto(0, 0)

    def bounce(self, context):
        # top
        if context == "top" or context == "paddle":
            self.setheading(360 - self.heading())
        #  top half of screen
        elif 180 > self.heading() >= 0:
            self.setheading(180 - self.heading())
        # bottom half
        elif 180 <= self.heading() < 360:
            self.setheading(540 - self.heading())
