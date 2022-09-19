from turtle import Turtle


# creating Paddle class which will inherit from Turtle class
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('sky blue')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(0, -270)

    def go_left(self):
        if self.xcor() >= -240:
            self.back(20)

    def go_right(self):
        if self.xcor() <= 230:
            self.forward(20)
