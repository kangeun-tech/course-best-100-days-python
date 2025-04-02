from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.write(f"Score : {self.score}", align="center", font=("Courier", 10, "normal"))
        self.penup()
        self.goto(0, 300)
        
    
    def add(self):
        self.score += 1
        self.write(f"Score : {self.score}", align="center", font=("Courier", 10, "normal"))
        

