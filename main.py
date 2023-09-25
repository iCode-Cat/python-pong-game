import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle_right = Paddle()
paddle_left = Paddle()
paddle_right.setposition(x=350, y=0)
paddle_left.setposition(x=-350, y=0)
pong_ball = Ball()
scoreboard = ScoreBoard()



screen.onkey(paddle_right.up,"Up")
screen.onkey(paddle_right.down,"Down")
screen.onkey(paddle_left.up,"w")
screen.onkey(paddle_left.down,"s")

game_is_on = True

while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move_right_top()

    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    if pong_ball.distance(paddle_right) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(paddle_left) < 50 and pong_ball.xcor() > -340:
        pong_ball.bounce_x()

    # Detect R paddle misses
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard.l_point()
        pong_ball.reset_speed()

    # Detect L paddle misses
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        scoreboard.r_point()
        pong_ball.reset_speed()

screen.exitonclick()