from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score_left = 0
        self.score_right = 0
        self.draw_score_left()
        self.draw_score_right()

        
    def draw_score_left(self) -> None:
        self.teleport(-50, 310)
        self.write(self.score_left, align="center", font=("Courier", 20, "bold"))
        
    def draw_score_right(self) -> None:
        self.teleport(50, 310)
        self.write(self.score_right, align="center", font=("Courier", 20, "bold"))
        