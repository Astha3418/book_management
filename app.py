from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8znxec]/'

# Load user data from JSON file
def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save user data to JSON file
def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    users = load_users()
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        # Here you can add code to set a session or cookie to track logged-in users
        return redirect(url_for('success'))
    else:
        flash('Invalid username or password', 'error')
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'Logged in successfully!'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users:
            flash('Username already exists!', 'error')
        else:
            users[username] = password
            save_users(users)
            flash('Account created successfully!', 'success')
            return redirect(url_for('index'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
