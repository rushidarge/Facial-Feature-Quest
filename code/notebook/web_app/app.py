from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Initialize an empty dataframe to store user selections
user_selections_df = pd.DataFrame(columns=['user_id', 'selected_image'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_options = int(request.form['num_options'])
        return render_template('select_option.html', num_options=num_options)

    return render_template('home.html')

@app.route('/select_option', methods=['POST'])
def select_option():
    selected_images = request.form.getlist('selected_image')
    
    # Retrieve user_id (for demo, using a simple increment)
    user_id = len(user_selections_df) + 1
    
    # Append the user selections to the dataframe
    for image in selected_images:
        user_selections_df.loc[len(user_selections_df)] = [user_id, image]
    
    return render_template('selected_option.html', selected_images=selected_images)

if __name__ == '__main__':
    app.run(debug=True)
