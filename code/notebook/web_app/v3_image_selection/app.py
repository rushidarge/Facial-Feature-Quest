from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

questions = {
    1: "Question 1?",
    2: "Question 2?",
    3: "Question 3?"
}

answers = {}

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    num_questions = int(request.form['num_questions'])
    for i in range(1, num_questions + 1):
        answer = request.form.get('answer{}'.format(i))
        answers['Question {}'.format(i)] = answer
    return render_template('answers.html', answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
