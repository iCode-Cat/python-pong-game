import turtle
from turtle import Turtle

MOVE_STEP = 10


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")



    def set_position(self, x, y):
        self.setposition(x, y)

    def up(self):
        self.setposition(x=self.xcor(), y=self.ycor() + MOVE_STEP)

    def down(self):
        self.setposition(x=self.xcor(), y=self.ycor() - MOVE_STEP)






