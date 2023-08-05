from turtle import Screen
from pongbars import PongBars, Borders
from ball import Ball
import time

DISTANCE = 20

screen = Screen()
border = Borders()
l_bar = PongBars(-492, 0)
r_bar = PongBars(488, 0)
b = Ball()

screen.setup(width=1020, height=510)
# screen.bgcolor("#24130c") DARK BACKGROUND
screen.bgcolor("#e4d7f3")  # LIGHT BACKGROUND
screen.title("Pong!")

border.make_border()
screen.tracer(0)


def trigger_up():
    l_bar.up()
    r_bar.up()


def trigger_down():
    l_bar.down()
    r_bar.down()


screen.listen()
screen.onkey(trigger_up, "Up")
screen.onkey(trigger_down, "Down")
screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.09)
    l_bar.move_pong_bars()
    r_bar.move_pong_bars()
    screen.update()

    b.move_ball()
    # Collision with wall
    if b.ycor() > 230 or b.ycor() < -230:
        b.setheading(360-b.heading())

    # Collision with pong_bars
    l_bar.check_dist(b)
    r_bar.check_dist(b)

screen.exitonclick()
