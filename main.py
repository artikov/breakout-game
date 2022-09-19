import time
import tkinter as tk
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from wall import Wall

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

# initializing scoreboard
scoreboard = Scoreboard()

# build wall
wall = Wall(3)

# listen to keys and move paddle
screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')


# check collision with brick
def check_brick_collision(brick):
    if abs((ball.xcor() - brick.xcor()) < 20 and brick.ycor() <= ball.ycor() <= brick.ycor() + 10):
        # print('hit the brick')
        print(brick.xcor(), brick.ycor())
        print(ball.xcor(), ball.ycor())
        ball.bounce_y()
        return True
    return False


# function to handle brick hit
def hit_brick(row):
    for x in range(len(row)):
        if check_brick_collision(row[x]):
            ball.bounce_y()
            print(row[x])
            row[x].goto(-1000, 1000)


# running game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detecting collision with side walls
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()
    # detect collision with top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    hit_brick(wall.wall_arr)

    # # TEMP check if ball collided with top wall
    # if ball.ycor() > 50:
    #     # scoreboard.upd_score()
    #     # can use as wall start position
    #     hit_brick(wall.wall_arr)
    #     ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -240:
        print('made contact')
        ball.bounce_y()

    # game loosing condition
    if ball.ycor() < -290:
        print('you loose')
        ball.reset_position()
        break


screen.exitonclick()

