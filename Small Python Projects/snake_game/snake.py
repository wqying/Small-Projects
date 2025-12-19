"""
Module that handles code related to the Snake
"""
from turtle import Turtle

# test


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, color="white", starting_positions=None):
        if starting_positions is None:
            starting_positions = STARTING_POSITIONS
        self.color = color
        self.segments = []
        self.create_snake(starting_positions)
        self.head = self.segments[0]

    def create_snake(self, starting_positions):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color(self.color)
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        """
        Gets the position of the most recently added snake object
        in the segment list and makes the body
        """
        self.add_segment((self.segments[-1].position()))

    def shrink(self):
        """
        Removes the last segment of the AI snake
        """
        if len(self.segments) > 2:
            tail = self.segments.pop()
            tail.hideturtle()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0,
                             -1):  # range can go backwards as well if we use negative for step
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def length(self):
        return len(self.segments)

    def positions_set(self):
        pos = set()
        for segment in self.segments:
            pos.add((int(segment.xcor()), int(segment.ycor())))
        return pos
    
    def next_cell(self, heading=None):
        if heading is None:
            heading = self.head.heading()
        x = int(self.head.xcor())
        y = int(self.head.ycor())
        if heading == UP:
            return (x, y + MOVE_DISTANCE)
        elif heading == DOWN:
            return (x, y - MOVE_DISTANCE)
        elif heading == LEFT:
            return (x - MOVE_DISTANCE, y)
        return (x + MOVE_DISTANCE, y)

    # player snake controls
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

