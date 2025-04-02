from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

my_ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(my_ball.move_speed)
    screen.update()
    my_ball.move()
    
    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()

    if my_ball.distance(r_paddle) < 50 and my_ball.xcor() > 320 or my_ball.distance(l_paddle) < 50 and my_ball.xcor() < -320:
        my_ball.bounce_x()

    if my_ball.xcor() > 380:
        my_ball.reset_position()
        scoreboard.l_point()

    if my_ball.xcor() < -380:
        my_ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()