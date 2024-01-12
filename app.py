from cs50 import SQL
from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, convert_currency, currency_rate, login_required


app = Flask(__name__)
db = SQL("sqlite:///exchange.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    currency = currency_rate("USD")
    return render_template("index.html", currency=currency)

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    name = request.form.get("name")
    last_name = request.form.get("last_name")
    confirmation = request.form.get("confirmation")
    dob = request.form.get("dob")
    username = request.form.get("username")
    password = request.form.get("password")

    if request.method == "POST":
        if not username or not password or not confirmation:
            return apology("INVALID USERNAME AND/OR PASSWORD", 400)
        if not name or not last_name or not dob:
            return apology("INVALID CREDENTIALS", 400)
        user = db.execute("SELECT * FROM users WHERE username = ?", username)
        
        if user:
            return apology("USERNAME ALREADY EXISTS", 400)     
        if password != confirmation:
            return apology("PASSWORDS DO NOT MATCH", 400)
        
        has_letters = any(c.isalpha() for c in password)
        has_numbers = any(c.isdigit() for c in password)
        has_alpha = any(not c.isalnum() for c in password)
        if not (has_letters and has_numbers and has_alpha):
            return apology("PASSWORD MUST CONTAIN AT LEAST ONE LETTER, ONE NUMBER AND ONE SPECIAL CHARACTER", 400)
        if len(password) < 8:
            return apology("PASSWORD MUST BE AT LEAST 8 CHARACTERS", 400)
        
        password = generate_password_hash(password)
        db.execute("INSERT INTO users (username, password, name, last_name, dob) VALUES (?, ?, ?, ?, ?)", username, password, name, last_name, dob)

        id = db.execute("SELECT id FROM users WHERE username = ?", username)[0]["id"]
        session["user_id"] = id
        return redirect("/")
    return render_template("sign_up.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = db.execute("SELECT * FROM users WHERE username = ?", username)
        
        if not username or not password:
            return apology("INVALID USERNAME AND/OR PASSWORD", 400)
        if len(user) != 1 or user[0]["username"] != username or not check_password_hash(user[0]["password"], password):
            return apology("INVALID USERNAME AND/OR PASSWORD")
        session["user_id"] = user[0]["id"]
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/login")
    
@app.route("/calculator", methods=["GET", "POST"])
@login_required
def calculator():
    source_currency = request.form.get("source_currency")
    target_currency = request.form.get("target_currency")
    amount = request.form.get("amount")

    if request.method == "POST":
        if not source_currency or not target_currency:
            return apology("INVALID CURRENCIES", 400)
        if not amount:
            return apology("INVALID AMOUNT", 400)
        if source_currency is None or target_currency is None:
            return apology("INVALID CURRENCY")
        # validate amount   
        try:
            amount = float(amount)
        except ValueError:
            return apology("INVALID AMOUNT", 400)
        if amount < 1.0:
            return apology("INVALID AMOUNT", 400)
        result = convert_currency(amount, source_currency, target_currency)
        db.execute("""INSERT INTO histories (user_id, source_currency, target_currency, amount, total, date_time)
                    VALUES (?, ?, ?, ?, ?, datetime('now'))""", session["user_id"], source_currency, target_currency, amount, result,)
        return render_template("quoted.html", source_currency=source_currency, target_currency=target_currency, amount=amount, result=result)
    
    rates = currency_rate("USD")
    return render_template("calculator.html", rates=rates)


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    users = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    return render_template("account.html", users=users)


@app.route("/delete_account", methods=["GET", "POST"])
@login_required
def delete_account(): 
    
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")
    users = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

    if request.method == "POST":
        if password != confirmation:
            return apology("INVALID PASSWORD", 400)
        if not check_password_hash(users[0]["password"], password):
            return apology("INVALID PASSWORD", 403)
        
        db.execute("DELETE FROM histories WHERE user_id = ?", session["user_id"])
        db.execute("DELETE FROM users WHERE id = ?", session["user_id"])
        session.clear()
        return redirect("/login")
    return render_template("delete.html")


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    current_password = request.form.get("current_password")
    new_password = request.form.get("new_password")
    new_password_confirmation = request.form.get("new_password_confirmation")
    users = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    
    if request.method == "POST":
        if not current_password or not new_password or not new_password_confirmation:
            return apology("INVALID PASSWORD", 400)
        if not check_password_hash(users[0]["password"], current_password):
            return apology("INVALID CURRENT PASSWORD")
        if new_password != new_password_confirmation:
            return apology("NEW PASSWORDS DO NOT MUCH", 400)
        if new_password == current_password:
            return apology("NEW PASSWORD MUST NOT BE SAME AS CURRENT PASSWORD", 400)
        has_letters = any(c.isalpha() for c in new_password)
        has_numbers = any(c.isdigit() for c in new_password)
        has_alpha = any(not c.isalnum() for c in new_password)
        if not (has_letters and has_numbers and has_alpha):
            return apology("PASSWORD MUST CONTAIN AT LEAST ONE LETTER, ONE NUMBER AND ONE SPECIAL CHARACTER", 400)
        if len(new_password) < 8:
            return apology("PASSWORD MUST BE AT LEAST 8 CHARACTERS", 400)
        new_password = generate_password_hash(new_password)
        db.execute("UPDATE users SET password = ? WHERE id = ?", new_password, session["user_id"])
        return redirect("/login")
        
    return render_template("change_password.html")


@app.route("/history")
@login_required
def history():
    histories = db.execute("SELECT * FROM histories WHERE user_id = ?", session["user_id"])
    return render_template("history.html", histories=histories)


@app.route("/contact", methods=["GET", "POST"])
@login_required
def contact():
    name = request.form.get("full_name")
    email = request.form.get("email")
    message = request.form.get("message")

    if request.method == "POST":
        if not name or not email or not message:
            return apology("INVALID MESSAGE", 400)
        if len(message) > 500 or len(message) < 0:
            return apology("MESSAGE MUST BE MINIMALLY 20 CHARACTERS OR 500 CHARACTERS LONG", 400)
        db.execute("INSERT INTO messages (name, email, message, date_time) VALUES (?, ?, ?, datetime('now'))", name, email, message)
        return redirect("/account")
    return render_template("contact.html")

    