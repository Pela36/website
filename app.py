from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Initialize the SQLite database
def init_db():
    if not os.path.exists("users.db"):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

init_db()

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash("Please log in to access this page.", "error")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists. Please choose another.', 'error')
        finally:
            conn.close()
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        conn.close()

        if result and check_password_hash(result[0], password):
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials, please try again.', 'error')
    return render_template('login.html')

# Dashboard route (protected page)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=session['user'])

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You've been logged out.", "success")
    return redirect(url_for('index'))

# Run the app on all available network interfaces
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
