from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
BTN_FONT = ("Courier", 16, "normal")


class ReplayButton:
    def __init__(self):
        self.t = Turtle()
        self.t.penup()
        self.t.hideturtle()
        # self.t.shapesize(stretch_wid=1.2, stretch_len=8.0)

    def show(self, on_click):
        self.t.clear()
        self.t.goto(0, -50)
        self.t.showturtle()
        self.t.stamp()
        self.t.pencolor("white")
        self.t.write("REPLAY", False, ALIGNMENT, BTN_FONT)
        self.t.onclick(lambda x, y: on_click())

    def hide(self):
        self.t.clear()
        self.t.onclick(None)
        self.t.hideturtle()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.count = 0
        self.replay_button = ReplayButton()
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score = {self.count}", False, ALIGNMENT, FONT)

    def update_score(self):
        self.count += 1
        self.show_score()

    def reset(self):
        self.count = 0
        self.replay_button.hide()
        self.show_score()

    def game_over(self, on_replay):
        self.goto(0, 0)
        self.write("GAME OVER! WOMP WOMP", False, ALIGNMENT,
                   FONT)
        self.replay_button.show(on_replay)
