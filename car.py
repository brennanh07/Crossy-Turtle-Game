from turtle import Turtle
import random

car_colors = ("red", "black", "blue", "orange", "green", "white", "purple")

lanes = [x for x in range(-260, 280, 20)]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2.2, stretch_wid=0.8)
        self.color(random.choice(car_colors))
        self.penup()
        self.sety(random.choice(lanes))
        self.setx(x=310)
        self.setheading(180)

    def move(self, level):
        speed = 10
        if level > 1:
            speed = speed + (level - 1) * 5
        self.forward(speed)



