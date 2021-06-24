from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
r_paddle.color("red")
l_paddle = Paddle((-350, 0))
l_paddle.color("blue")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
paddle_hit = 0
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if paddle_hit == 0 and (ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and
                            ball.distance(l_paddle) < 50):
        ball.bounce_x()
        paddle_hit = 1
    elif -320 < ball.xcor() < 320:
        paddle_hit = 0

    # Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
