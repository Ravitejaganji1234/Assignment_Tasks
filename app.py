from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mahi3437',
    database='at'
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    dob = request.form['dob']
    cursor.execute("INSERT INTO users (name, email, age, dob) VALUES (%s, %s, %s, %s)", (name, email, age, dob))
    db.commit()
    return redirect('/users')

@app.route('/users')
def display_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('user_table.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
