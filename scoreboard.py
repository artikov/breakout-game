from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.level = 0
        self.high_score = 0
        self.goto(0, 250)
        self.upd_scoreboard()

    def upd_scoreboard(self):
        self.clear()
        self.write(self.score, align='center', font=('courier', 50, 'normal'))

    def upd_score(self):
        self.score += 1
        self.upd_scoreboard()

