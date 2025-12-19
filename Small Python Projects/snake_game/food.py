from turtle import Turtle
import random

BOUNDS = 250


class Food(Turtle):
    """
    An object that represents "food" the snake is chasing after
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-BOUNDS, BOUNDS)
        random_y = random.randint(-BOUNDS, BOUNDS)
        self.goto(random_x, random_y)

