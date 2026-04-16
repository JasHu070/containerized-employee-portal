from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "/app/data/employees.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def get_employees():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT name, role FROM employees")
    rows = cursor.fetchall()

    conn.close()
    return rows

@app.route("/")
def home():
    employees = get_employees()
    return render_template("index.html", employees=employees)

@app.route("/add", methods=["POST"])
def add_employee():
    name = request.form["name"]
    role = request.form["role"]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employees (name, role) VALUES (?, ?)",
        (name, role)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == "__main__":
    os.makedirs("/app/data", exist_ok=True)
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
