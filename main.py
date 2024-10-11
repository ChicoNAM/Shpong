# 2024 - 10 - 10 | Pong Game
from paddle import Paddle
from ball import Ball
from board import Board
import time
from scoreboard import Scoreboard
from gamewindow import GameWindow

game_window = GameWindow()
game_board = Board()
scoreboard = Scoreboard()
player1 = Paddle(350,0)
player2 = Paddle(-350,0)
ball = Ball()


def game():

    game_window.screen.listen()
    game_window.screen.onkeypress(player1.move_up,"Up")
    game_window.screen.onkeypress(player1.move_down,"Down")
    game_window.screen.onkeypress(player2.move_up,"w")
    game_window.screen.onkeypress(player2.move_down,"s")

    flag = True

    while flag == True:
        game_window.screen.update()
        time.sleep(0.01)
        ball.move()
        if ball.ycor() > 290:
            ball.sety(290)
            ball.y_direction *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.y_direction *= -1
        if ball.xcor() > 390:
            ball.teleport(0,0)
            ball.x_direction *= -1
            scoreboard.clear()
            scoreboard.score_left += 1
            scoreboard.draw_score_left()
            scoreboard.draw_score_right()
        if ball.xcor() < -390:
            ball.teleport(0,0)
            ball.x_direction *= -1
            scoreboard.clear()
            scoreboard.score_right += 1
            scoreboard.draw_score_right()
            scoreboard.draw_score_left()
            
        if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
            ball.setx(340)
            ball.x_direction *= -1
            
        if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
            ball.setx(-340)
            ball.x_direction *= -1
            
        if scoreboard.score_left == 10:
            scoreboard.clear()
            scoreboard.draw_game_over()
            flag = False
            
        if scoreboard.score_right == 10:
            scoreboard.clear()
            scoreboard.draw_game_over()
            flag = False

if __name__ == "__main__":
    game()

game_window.screen.exitonclick()