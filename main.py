import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
Scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    
    # detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            Scoreboard.game_over()
            
            
    # successful pass
    if player.is_at_finish_line():
        player.goto_start()
        Scoreboard.update_level()
        cars.level_up()
        
screen.exitonclick()
