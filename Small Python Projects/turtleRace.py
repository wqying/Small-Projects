from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -230
y = -100
all_turtles = []
finish_line = False

for turtles_number in range(6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtles_number])
    turtle.goto(x=x, y=y)
    y += 40
    all_turtles.append(turtle)

while not finish_line:
    for turtles in all_turtles:
        step = random.randint(0, 10)
        turtles.forward(step)
        if turtles.xcor() >= 230:
            finish_line = True
            winner = turtles.pencolor()
            if winner == user_bet.lower():
                print(f"You win! {winner} is the winner.")
            else:
                print(f"You lose! {winner} is the winner.")
            break


screen.exitonclick()
