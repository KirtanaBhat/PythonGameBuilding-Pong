from turtle import Turtle
import random

DISTANCE = 25
random_start = [random.randint(30, 60), random.randint(100, 130), random.randint(210, 240), random.randint(280, 310)]
angle = random.choice(random_start)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.7)
        self.color("black")
        self.penup()
        self.goto(0, random.randint(-230, 231))
        self.setheading(angle)

    def move_ball(self):
        self.forward(DISTANCE)
