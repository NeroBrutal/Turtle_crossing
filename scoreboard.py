from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_level()
        
    def update_level(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f"Level:{self.level}", align="center", font=FONT)
        self.level += 1
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center" , font=FONT)
        
    
        
