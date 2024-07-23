from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.points} ",move=False,align="center",font=("Arial",18,"normal"))

    def update(self):
        self.points +=1
        self.clear() 
        self.write(f"Score: {self.points} ",move=False,align="center",font=("Arial",18,"normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER \n your Score: {self.points}",move=False,align="center",font=("Arial",28,"normal"))