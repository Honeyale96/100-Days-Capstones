from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)
screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)

#Net
place_y = 325
for _ in range(15):
    place_y -= 40
    place = (0, place_y)
    t = Turtle()
    t.shape("square")
    t.shapesize(stretch_wid=1, stretch_len=0.5)
    t.color("white")
    t.pu()
    t.goto(place)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
