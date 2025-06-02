from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.ht()
        self.penup()
        self.count = 0
        self.show_score()

    def show_score(self):
        self.goto(0, 260)
        self.write(f"Score = {self.count}", False, ALIGNMENT,
                   FONT)

    def update_score(self):
        self.count += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER! WOMP WOMP", False, ALIGNMENT,
                   FONT)


