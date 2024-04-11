# from flask import Flask, render_template, request
import pandas as pd
import random

df = pd.read_csv(r'D:\Projects\Face_analysis_game\code\notebook\web_app\v3.1_quiz\static\test.csv')
# return df

def generate_questions(data, num_questions):
    print('Generating questions...')
    questions = []
    # Shuffle the data to ensure randomness
    data = data.sample(frac=1).reset_index(drop=True)
    print('After Shuffling data...')
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
        incorrect_choices = incorrect_rows.copy()
        print('we get the incorrect choices', incorrect_choices)
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
    
    print(questions)
    return questions

generate_questions(df,3)