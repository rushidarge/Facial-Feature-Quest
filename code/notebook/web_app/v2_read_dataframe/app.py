# app.py
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Read CSV file into DataFrame
csv_path = r'D:\Projects\Face_analysis_game\code\notebook\web_app\v2_read_dataframe\static\Facial feature quiz_demo_sheet.csv' 
df = pd.read_csv(csv_path)


@app.route('/')
def home():
    # Get unique person names
    person_names = df['person name'].unique()
    return render_template('home.html', person_names=person_names)


@app.route('/filter', methods=['POST'])
def filter_data():
    # Get selected person name from the form
    selected_person = request.form['person']

    # Filter DataFrame based on the selected person
    filtered_data = df[df['person name'] == selected_person]

    # Pass filtered data to the next page
    image_paths = filtered_data['image path'].tolist()
    return render_template('filtered.html', image_paths=image_paths)


if __name__ == '__main__':
    app.run(debug=True)
