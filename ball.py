from turtle import Turtle

SPEED = 10

class Ball(Turtle):
    def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_direction = 2
        self.y_direction = 2
        
    def move(self) -> None:
        self.setx(self.xcor() + self.x_direction)
        self.sety(self.ycor() + self.y_direction)
        self.speed(SPEED)
