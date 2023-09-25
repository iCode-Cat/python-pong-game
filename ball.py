from turtle import Turtle
MOVE_STEP = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color("white")
        self.speed(0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_right_top(self):
        x_pos = self.xcor() + self.x_move
        y_pos= self.ycor() + self.y_move
        self.goto(x=x_pos, y=y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_speed(self):
        self.move_speed = 0.1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()




