from turtle import Turtle

class Board(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.pensize(2)
        self.color("white")
        self.setheading(270)
        self.draw_left_line()
        self.draw_mid_line()
        self.draw_right_line()
        self.draw_top_line()
        self.draw_bottom_line()
    
    def draw_left_line(self) -> None:
        self.teleport(-350,300)
        for _ in range(15):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
            
    def draw_mid_line(self) -> None:
        self.teleport(0,300)
        for _ in range(15):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
            
    def draw_right_line(self) -> None:
        self.teleport(350,300)
        for _ in range(15):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()

    def draw_top_line(self) -> None:
        self.teleport(-350,300)
        self.left(90)
        for _ in range(18):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
            
    def draw_bottom_line(self) -> None:
        self.teleport(-350,-300)
        for _ in range(18):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()