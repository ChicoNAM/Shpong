from turtle import Turtle

MOVEMENT_SPEED = 20

class Paddle(Turtle):
    def __init__(self, x_position, y_position, shape = "square", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.x_position = x_position
        self.y_position = y_position
        self.hideturtle()
        self.teleport(x_position,y_position)
        self.color("white")
        self.left(90)
        self.shapesize(1,4,1)
        self.penup()
        self.speed("fastest")
        self.showturtle()
        
    def move_up(self) -> None:
        self.forward(MOVEMENT_SPEED)
        
    def move_down(self) -> None:
        self.backward(MOVEMENT_SPEED)
