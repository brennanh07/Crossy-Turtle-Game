from turtle import Screen
import time
from player import Player
from car import Car
from scoreboard import Scoreboard
from road import Road, coordinates


def spawn_car():
    car = Car()
    cars.append(car)
    screen.ontimer(spawn_car, 500)


level = 1

cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)
screen.listen()

for coordinate in coordinates:
    road = Road(coordinate)

player = Player()

scoreboard = Scoreboard()

bindings = {
    "w": player.move_forward,
    "s": player.move_backward,
    "a": player.move_left,
    "d": player.move_right,
}

spawn_car()

play_game = True
while play_game:
    scoreboard.update(level)
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move(level)
        if car.distance(player) < 20:
            play_game = False

    for key, func in bindings.items():
        screen.onkeypress(key=key, fun=func)

    if player.ycor() >= 280:
        level += 1
        player.teleport(x=0, y=-300)



screen.exitonclick()



