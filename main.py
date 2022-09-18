import tkinter as tk
from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

# game screen initialized
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Breakout')
screen.tracer(0)

# initializing paddle object
paddle = Paddle()

# initializing ball object
ball = Ball()

screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detecting collision with side walls
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    # TEMP check if ball collided with top wall
    if ball.ycor() > 150: # can use as wall start position
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -240: # 320
        print('made contact')
        ball.bounce_y()

    # game winning and loosing conditions
    if ball.ycor() > 300:
        print('player won')
        break
    if ball.ycor() < -290:
        print('you loose')
        ball.reset_position()
        # break


screen.exitonclick()

