from flask import Flask, render_template
import random
from datetime import datetime
import requests


app = Flask(__name__)
NAME = "Ying Wong"

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    # note that this file has to be in "templates" for Flask!
    return render_template("index.html",
                           num=random_number,
                           year=current_year,
                           name=NAME)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html",
                           name=name,
                           gender=gender,
                           age=age)

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/652c8dc7ec8b4d903416"
    response = requests.get(blog_url)
    all_posts = response.json()  # use for loop in the blog.html using jinja
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


