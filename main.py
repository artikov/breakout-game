import tkinter as tk
from turtle import Screen
from paddle import Paddle

# game screen initialized
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Breakout')

# initializing paddle object
paddle = Paddle()


screen.exitonclick()

