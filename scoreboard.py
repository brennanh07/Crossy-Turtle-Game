from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.teleport(x=0, y=275)
        self.hideturtle()

    def update(self, level):
        self.clear()
        self.write(f"Level: {level}", align="center", font=("Arial", 16, "bold"))
