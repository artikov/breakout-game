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
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')
screen.listen()


# check collision with brick
def check_brick_collision(brick):
    if abs(ball.xcor() - brick.xcor()) < 20 and brick.ycor() <= ball.ycor() <= brick.ycor() + 10:
        return True
    return False


# function to handle brick hit
def hit_brick(row):
    for x in range(len(row)):
        if check_brick_collision(row[x]):
            ball.bounce('')
            scoreboard.upd_score()
            row[x].goto(-1000, 1000)


# running game
game_is_on = True
while game_is_on:
    # time.sleep(0.1)
    screen.update()
    # ball.move()
    ball.forward(5)

    # detecting collision with side walls
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce('')
    # detect collision with top wall
    if ball.ycor() > 280:
        ball.bounce('top')

    hit_brick(wall.wall_arr)

    # detect collision with paddle
    # if ball.distance(paddle) < 50 and ball.ycor() < -250:
    if abs(ball.xcor() - paddle.xcor() < 50) and paddle.ycor() <= ball.ycor() <= paddle.ycor() + 20:
        ball.bounce('paddle')

    # game loosing condition
    if ball.ycor() < -290:
        print('you loose')
        ball.reset_position()
        # break

    screen.update()


screen.exitonclick()

