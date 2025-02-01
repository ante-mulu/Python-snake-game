import turtle
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highscore}" , align="center", font=("Arial", 18, "bold"))
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

