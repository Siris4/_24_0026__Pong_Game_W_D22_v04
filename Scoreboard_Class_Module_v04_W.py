
from turtle import Turtle
# from __2x__Pong_Game_Main_v02_W__231027 import p1_scoreboard_location, p2_scoreboard_location

#CONSTANTS:
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self, scoreboard_position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.r_p1_score = 0
        self.l_p2_score = 0
        self.goto(100, 270)
        # self.write_the_scoreboard_for_p1()
        self.write(f"P1 Score: {self.r_p1_score}", align=ALIGNMENT, font=("Courier", 16, "normal"))
        self.goto(-100, 270)
        self.write(f"P2 Score: {self.l_p2_score}", align=ALIGNMENT, font=("Courier", 16, "normal"))
        # self.write_the_scoreboard_for_p2()


    # def write_the_scoreboard_for_p1(self):
    #     self.clear()
    #     self.write(f"P1 Score: {self.r_p1_score}", align=ALIGNMENT, font=("Courier", 16, "normal"))

    # def write_the_scoreboard_for_p2(self):
    #     self.clear()
    #     self.write(f"P2 Score: {self.l_p2_score}", align=ALIGNMENT, font=("Courier", 16, "normal"))

    # def update_score(self):
    #     self.score += 1
    #     self.clear()
    #     self.write_the_scoreboard()
    #
    # def game_over_display_for_p1(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER PLAYER 1. PLAYER 2 WINS.", move=False, align=ALIGNMENT, font=FONT)
    #
    # def game_over_display_for_p2(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER PLAYER 2. PLAYER 1 WINS.", move=False, align=ALIGNMENT, font=FONT)



