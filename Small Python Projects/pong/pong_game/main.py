from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#800 x 600

TOP_WALL = 280
BOTTOM_WALL = -280

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


paddle_1 = Paddle(-350, 0)
paddle_2 = Paddle(350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle_2.go_up, "Up")
screen.onkey(paddle_2.go_down, "Down")
screen.onkey(paddle_1.go_up, "w")
screen.onkey(paddle_1.go_down, "s")

def check_collision_with_walls(ball):
    if ball.ycor() > TOP_WALL or ball.ycor() < BOTTOM_WALL:
        return True
    return False

def check_collision_with_paddle(ball, left_paddle, right_paddle):
    if ball.distance(left_paddle) < 50 and (ball.xcor() < -320):
        return True
    if ball.distance(right_paddle) < 50 and (ball.xcor() > 320):
        return True
    return False

def ball_out_of_bounds(ball):
    if ball.xcor() > 400:
        score.l_point()
        return True
    if ball.xcor() < -400:
        score.r_point()
        return True
    return False


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed) # slow down the ball movement
    screen.update() # because tracer is turned off at the start
    ball.move()
    if check_collision_with_walls(ball):
        ball.bounce_y()
    if check_collision_with_paddle(ball, paddle_1, paddle_2):
        ball.bounce_x()
    if ball_out_of_bounds(ball):
        ball.reset_ball()
        ball.bounce_x()
        ball.bounce_y()


screen.exitonclick()