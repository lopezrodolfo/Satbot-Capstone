import sqlite3
import uuid

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from NN.bot import conversate
from NN.train import train

app = Flask(__name__)
app.secret_key = "your_secret_key"


def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        classcode TEXT,
        is_admin INTEGER DEFAULT 0
    )"""
    )
    conn.commit()
    conn.close()


init_db()


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[4], password):
            session["username"] = username
            session["is_admin"] = user[6]
            if user[6]:
                return redirect(url_for("admin"))
            else:
                return redirect(url_for("chat"))
        else:
            flash("Invalid Credentials", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]
        is_admin = request.form.get("is_admin") == "on"

        if password != confirm_password:
            flash("Passwords do not match", "danger")
            return redirect(url_for("signup"))

        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
        classcode = str(uuid.uuid4()) if is_admin else request.form["classcode"]

        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (firstname, lastname, username, password, classcode, is_admin) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    firstname,
                    lastname,
                    username,
                    hashed_password,
                    classcode,
                    int(is_admin),
                ),
            )
            conn.commit()
            conn.close()
            flash("Account created successfully", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username already exists", "danger")
            return redirect(url_for("signup"))

    return render_template("signup.html")


@app.route("/validate_classcode")
def validate_classcode():
    classcode = request.args.get("classcode")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM users WHERE classcode = ?", (classcode,))
    exists = cursor.fetchone() is not None
    conn.close()
    return {"valid": exists}


@app.route("/chat")
def chat():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("chatscreen.html")


@app.route("/admin")
def admin():
    if "username" not in session or not session.get("is_admin"):
        return redirect(url_for("login"))

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT classcode FROM users WHERE username = ?", (session["username"],)
    )
    classcode = cursor.fetchone()[0]
    conn.close()

    return render_template("admin.html", classcode=classcode)


@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = conversate(user_message)
    return bot_response


@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("is_admin", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    train()
    app.run()
