from turtle import Turtle, Screen

import pygame

from score import Scoreboard
from paddles import Paddle
from ball import Ball
from pygame import *
import time

mixer.init()
ping = mixer.Sound("ping.wav")
funny = mixer.Sound("lost-closing-credits.mp3")

score = Scoreboard()
ball = Ball()
screen = Screen()
r_paddle = Paddle((350, 0), '#B03F47')
l_paddle = Paddle((-350, 0), '#50A859')
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("#313837")

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game = True
while game:
    time.sleep(ball.speedd)
    screen.update()
    ball.move()
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < r_paddle.ycor() + 60 and ball.ycor() > r_paddle.ycor() - 60):
        ball.bounce_off_paddle()
        ping.play()
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < l_paddle.ycor() + 60 and ball.ycor() > l_paddle.ycor() - 60):
        ball.bounce_off_paddle()
        ping.play()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    if ball.xcor() > 390:
        funny.play()
        score.point1()
        ball.refresh()
    if ball.xcor() < -390:
        # funny.play()
        ball.refresh()
        score.point2()

screen.exitonclick()
