''' 
app.py - Main application file for the Flask web app.

'''
import os
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# --- Configuration ---
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

#--- Routes ---
@app.route('/')
def home():
    "Renders the main homepage."
    return render_template('index.html')

@app.route('/blog')
def blog_list():
    return render_template('index.html', active_section='blog')

@app.route('/projects')
def projects_list():
    return render_template('index.html' , active_section = 'projects')


# --- Run the application --- 
if __name__ =='__main__':
    print("Starting Flask application...")
    app.run(debug = True)

