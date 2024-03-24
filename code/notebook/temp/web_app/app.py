from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Initialize an empty dataframe to store user selections
user_selections_df = pd.DataFrame(columns=['user_id', 'selected_image'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select_option', methods=['GET', 'POST'])
def select_option():
    if request.method == 'POST':
        selected_image = request.form['selected_image']
        
        # Retrieve user_id (for demo, using a simple increment)
        user_id = len(user_selections_df) + 1
        
        # Append the user selection to the dataframe
        user_selections_df.loc[len(user_selections_df)] = [user_id, selected_image]
        
        return render_template('selected_option.html', selected_image=selected_image)

    return render_template('select_option.html')

if __name__ == '__main__':
    app.run(debug=True)
