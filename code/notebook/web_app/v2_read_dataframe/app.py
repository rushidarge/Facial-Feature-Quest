from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Function to read CSV data and filter images
def process_images():
    csv_path = r'D:\Projects\Face_analysis_game\code\notebook\web_app\v2_read_dataframe\static\Facial feature quiz_demo_sheet.csv'  # Update with your CSV file path
    df = pd.read_csv(csv_path)
    
    print(df)

    # Apply filters to the DataFrame as needed
    filtered_df = df[(df['type'] == 'eye') & (df['gender'] == 'male')]
    
    # Select four images
    selected_images = filtered_df['image path'].head(4).tolist()
    
    return selected_images

# Route to display images
@app.route('/quiz')
def quiz():
    images = process_images()
    return render_template('quiz.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
