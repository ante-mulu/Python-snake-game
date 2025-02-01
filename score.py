import turtle
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            highest=data.read()
        self.score= 0
        self.highscore=int(highest)
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
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

