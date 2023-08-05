from turtle import Turtle
import random

DISTANCE = 20

class Borders(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        # self.color("white")
        self.color("black")
        self.pensize(3)
        self.setheading(90)
        self.goto(0, -250)

    def make_border(self):
        for _ in range(0, 20):
            self.forward(12)
            self.pendown()
            self.forward(13)
            self.penup()
        self.hideturtle()


class PongBars(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.new_bar = Turtle("square")
        # new_bar.color("white")
        self.new_bar.color("black")
        self.new_bar.shapesize(stretch_wid=1, stretch_len=5)
        self.new_bar.penup()
        self.new_bar.speed("fastest")
        self.new_bar.goto(self.x, self.y)
        self.new_bar.setheading(90)

    def move_pong_bars(self):
        if self.new_bar.ycor() > 197:
            self.new_bar.setheading(270)
        elif self.new_bar.ycor() < -197:
            self.new_bar.setheading(90)
        self.new_bar.forward(DISTANCE)

    def up(self):
        if self.new_bar.heading() != 90:
            self.new_bar.setheading(90)

    def down(self):
        if self.new_bar.heading() != 270:
            self.new_bar.setheading(270)

    def check_dist(self, b):
        if b.distance(self.new_bar) < 45 and (b.xcor() > 470 or b.xcor() < -470):
            b.setheading(180 - b.heading())

        elif b.xcor() > 540 or b.xcor() < -540:
            b.goto(0, random.randint(-230, 231))
