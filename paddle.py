from turtle import Turtle


# creating Paddle class which will inherit from Turtle class
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(0, -270)
