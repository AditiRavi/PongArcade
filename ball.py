import turtle as t
import random
COLORS = ["royal blue", "blue", "cyan", "darkorchid", "fuchsia", "purple1", "violet", "aquamarine1", "blue violet"]


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.color(random.choice(COLORS))
        self.bounce_x()
        self.move_speed = 0.1
