from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__() # use everything from the Turtle class
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + 20 # move 20 pixels
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20 # move 20 pixels
        self.goto(self.xcor(), new_y)