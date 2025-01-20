import turtle as t
import time
from paddle import Paddle
from ball import Ball
from scorecard import Score

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong_ball = Ball((0,0))
score = Score()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()

    # detecting the collision with the wall
    if pong_ball.ycor()>280 or pong_ball.ycor() <-280:
        pong_ball.bounce_y()
    # detecting collision with the paddle
    if pong_ball.distance(r_paddle)< 50 and pong_ball.xcor() > 330 or pong_ball.distance(l_paddle)< 50 and pong_ball.xcor()< -330:
        pong_ball.bounce_x()

    # detecting the r_paddle miss
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        score.l_point()

    # detecting the l_paddle miss
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        score.r_point()


screen.exitonclick()
