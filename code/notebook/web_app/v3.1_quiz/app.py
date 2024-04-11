from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Function to read CSV file and return data
def read_csv(file_path):
    df = pd.read_csv(r'D:\Projects\Face_analysis_game\code\notebook\web_app\v3.1_quiz\static\test.csv')
    return df

# Function to generate multiple-choice questions
import random

def generate_questions(data, num_questions):
    # print('Generating questions...')
    questions = []
    # Shuffle the data to ensure randomness
    data = data.sample(frac=1).reset_index(drop=True)
    # print('After Shuffling data...')
    for i in range(num_questions):
        # Select a random row from the shuffled data
        selected_row = data.iloc[i]
        correct_img_path = selected_row['img_path']
        ground_truth = selected_row['ground_truth']
        img_size = selected_row['img_size']
        
        # Randomly select three incorrect image paths
        incorrect_rows = [row for i, row in data.iterrows() if row['img_path'] != correct_img_path]
        # shuffle the incorrect list
        random.shuffle(incorrect_rows)
        incorrect_choices = incorrect_rows[:3]
        # print('we get the incorrect choices', incorrect_choices)
        # Create a list of options including the correct and incorrect image paths
        options = [correct_img_path]
        options.extend([row['img_path'] for row in incorrect_choices])
        
        # Shuffle the options to randomize their order
        options = random.sample(options, len(options))
        
        # Create a dictionary for the question
        question = {
            'question': f"What is the image path for {ground_truth} of size {img_size}?",
            'correct_answer': correct_img_path,
            'options': options
        }
        questions.append(question)
    
    # print(questions)
    return questions


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Get user input (number of questions)
        num_questions = int(request.form['num_questions'])

        # Read CSV file and select random subset of questions
        csv_path = 'D:\Projects\Face_analysis_game\code\notebook\web_app\v2_read_dataframe\static\Facial feature quiz_demo_sheet.csv' 
        data = read_csv(csv_path)
        print(data)
        questions = generate_questions(data, num_questions)

        return render_template('quiz.html', questions=questions)
    return render_template('quiz_start.html')

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    if request.method == 'POST':
        # Get user's answers from the form
        user_answers = {}
        print('###   ###  '*3)
        print(request.form)
        for key, value in request.form.items():
            if key.startswith('answer'):
                question_number = int(key.replace('answer', ''))
                user_answers[question_number] = value

        # Get correct answers from hidden fields
        correct_answers = {}
        for key, value in request.form.items():
            if key.startswith('question'):
                question_number = int(key.replace('question', ''))
                correct_answers[question_number] = value

        # Compare user's answers with correct answers and calculate accuracy
        num_correct = 0
        for question_number, correct_answer in correct_answers.items():
            if user_answers.get(question_number) == correct_answer:
                num_correct += 1

        accuracy = (num_correct / len(correct_answers)) * 100

        return render_template('quiz_result.html', accuracy=accuracy)


if __name__ == '__main__':
    app.run(debug=True)
