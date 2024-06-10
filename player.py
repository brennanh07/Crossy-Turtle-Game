from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=0.9)
        self.color("green")
        self.penup()
        self.teleport(y=-300)
        self.setheading(90)

    def move_forward(self):
        self.setheading(90)
        self.forward(20)

    def move_backward(self):
        self.setheading(270)
        self.forward(20)

    def move_left(self):
        self.setheading(180)
        self.forward(20)

    def move_right(self):
        self.setheading(0)
        self.forward(20)

