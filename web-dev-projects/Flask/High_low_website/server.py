from flask import Flask
import random

app = Flask(__name__)
ran_num = random.randint(0, 9)
print(ran_num)

@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHE3ZmU3YmZ5Z2VhZHltcGdrdDdzeHU5bnhmZHJwcDlsMHVwNDBicSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GOaMRxfIqqnvbfF84h/giphy.gif">'

@app.route("/<int:user_num>")  # flask uses <> for variables in route!
def guess(user_num):
    if user_num == ran_num:
        return '<h1 style="color: green;">You found me!</h1>' \
                '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGMyOXE1NDU5cTNyM2Q5OGxkMGxpbnh3cXA3OTA4ajFqaHVoYjVzdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EM76SUKIS2pt5EhB01/giphy.gif">'
    elif user_num < ran_num:
        return '<h1 style="color: red;">Too low, try again!</h1>' \
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWg0NnAwdGttNXkyYWpqZ2ltcGd5ZHF2NmttM2N1YnFtMTVoa3RjayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Wye2tGoqEgyvZpQEXH/giphy.gif">'
    elif user_num > ran_num:
        return '<h1 style="color: purple;">Too high, try again!</h1>' \
                '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd291bTVybW51dGl3N2tqc3QwNnR1dXoyaDdxdDViZHZqcHBkMjA1OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zI6H8qp3eSgqLECZFo/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=False)