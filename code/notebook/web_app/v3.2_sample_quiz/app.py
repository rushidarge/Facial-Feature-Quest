from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Load questions from questions.py
from questions import questions

current_question = 0
score = 0

@app.route('/')
def index():
    global current_question
    current_question = 0  # Reset question index for new game
    global score
    score = 0  # Reset score for new game
    return render_template('index.html', question=questions[current_question], current_question=current_question)


@app.route('/answer', methods=['POST'])
def answer():
    global current_question, score
    selected_answer = request.form['answer']
    correct_answer = questions[current_question]['correct_answer']

    if selected_answer == correct_answer:
        score += 1

    current_question += 1  # Update current_question regardless of answer

    if current_question >= len(questions):
        accuracy = score / len(questions) * 100
        return render_template('result.html', accuracy=accuracy)
    else:
        return render_template('index.html', question=questions[current_question])


if __name__ == '__main__':
    app.run(debug=True)
