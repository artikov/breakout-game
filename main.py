import tkinter as tk
from turtle import Screen
from ball import Ball
from brick import Brick
from paddle import Paddle
import time

# game screen initialized
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Breakout')
screen.tracer(0)

# initializing paddle object
paddle = Paddle()

# initializing ball object
ball = Ball()

# initializing scoreboard
scoreboard = Scoreboard()


# building wall
def build_wall(y, color):
    wall_arr = []
    for x in range(-275, 290, 45):
        wall_arr.append(Brick(x, y, color))
    return wall_arr


# colors = ["sky blue", "tomato", "lime green","yellow"]
wall_pos = 150
wall = build_wall(wall_pos, 'lime green')
wall2 = build_wall(125, 'green')
# LOGIC TO CHECK COLLISION WITH BRICK
print(wall[0].xcor())
wall[3].goto(-1000, 1000)

# listen to keys and move paddle
screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')

# running game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detecting collision with side walls
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    # TEMP check if ball collided with top wall
    if ball.ycor() > 150:
        scoreboard.upd_score()
        # can use as wall start position
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -240:
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

