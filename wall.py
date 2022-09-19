import random
from brick import Brick

colors = ["sky blue", "tomato", "lime green", "yellow"]


class Wall:
    def __init__(self, rows):
        self.wall_pos = 175
        self.row = 25
        self.rows = rows
        self.wall_arr = []
        self.build_wall()

    # building wall
    def build_wall(self):
        for r in range(self.rows):
            self.wall_pos -= 25
            color = random.choice(colors)
            for x in range(-275, 290, 45):
                self.wall_arr.append(Brick(x, self.wall_pos, color))
        return self.wall_arr

