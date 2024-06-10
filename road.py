from turtle import Turtle

x_coordinates = [x for x in range(-300, 300, 28)]
y_coordinates = [y for y in range(-270, 270, 20)]

coordinates = [(x, y) for x in x_coordinates for y in y_coordinates]


class Road(Turtle):

    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.shapesize(stretch_len=1, stretch_wid=0.1)
        self.teleport(x=location[0], y=location[1])
