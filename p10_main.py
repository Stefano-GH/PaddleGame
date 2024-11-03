# Import libraries
from turtle import Screen
from p10_paddle import Paddle
from p10_ball import Ball
from p10_scoreboard import Scoreboard
import time


# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# Set the initial settings
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "a")
screen.onkey(l_paddle.go_down, "z")


# Let's game!
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect wall collision
    if not abs(ball.ycor()) < 280:
        ball.y_bounce()
    
    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    
    # Detect R paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    
    # Detect L paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()