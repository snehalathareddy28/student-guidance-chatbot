if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template, request, redirect, url_for, session
from logic.guidance_engine import get_guidance
from database.db import init_db, save_student, init_user_db, register_user, validate_user
from logic.chatbot_engine import generate_response  # <-- add this line
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this in production!

# Initialize databases
init_db()
init_user_db()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template, request, redirect, url_for, session
from logic.guidance_engine import get_guidance
from database.db import init_db, save_student, init_user_db, register_user, validate_user
from logic.chatbot_engine import generate_response  # <-- add this line
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this in production!

# Initialize databases
init_db()
init_user_db()

# -------------------- HOME --------------------
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("form"))
    return redirect(url_for("login"))

# -------------------- REGISTER --------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if register_user(username, password):
            return redirect(url_for("login"))
        else:
            return "Username already exists! Please choose another."
    return render_template("register.html")

# -------------------- LOGIN --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if validate_user(username, password):
            session["username"] = username
            return redirect(url_for("form"))
        else:
            return "Invalid credentials! Try again."
    return render_template("login.html")

# -------------------- LOGOUT --------------------
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

# -------------------- STUDENT FORM --------------------
@app.route("/form", methods=["GET", "POST"])
def form():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("form.html")

# -------------------- RESULT --------------------
@app.route("/result", methods=["POST"])
def result():
    if "username" not in session:
        return redirect(url_for("login"))
    name = request.form.get("name")
    education = request.form.get("education")
    stream = request.form.get("stream")
    interest = request.form.get("interest")

    # Save student info in DB
    save_student(name, education, stream, interest)

    # Get guidance
    guidance = get_guidance(education, stream, interest)
    return render_template("result.html", name=name, guidance=guidance)

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    if "username" not in session:
        return redirect(url_for("login"))
    
    response = ""
    if request.method == "POST":
        user_message = request.form.get("message")
        response = generate_response(user_message)
    
    return render_template("chatbot.html", response=response)


# -------------------- RUN APP --------------------
if __name__ == "__main__":
    app.run(debug=True)

# -------------------- HOME --------------------
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("form"))
    return redirect(url_for("login"))

# -------------------- REGISTER --------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if register_user(username, password):
            return redirect(url_for("login"))
        else:
            return "Username already exists! Please choose another."
    return render_template("register.html")

# -------------------- LOGIN --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if validate_user(username, password):
            session["username"] = username
            return redirect(url_for("form"))
        else:
            return "Invalid credentials! Try again."
    return render_template("login.html")

# -------------------- LOGOUT --------------------
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

# -------------------- STUDENT FORM --------------------
@app.route("/form", methods=["GET", "POST"])
def form():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("form.html")

# -------------------- RESULT --------------------
@app.route("/result", methods=["POST"])
def result():
    if "username" not in session:
        return redirect(url_for("login"))
    name = request.form.get("name")
    education = request.form.get("education")
    stream = request.form.get("stream")
    interest = request.form.get("interest")

    # Save student info in DB
    save_student(name, education, stream, interest)

    # Get guidance
    guidance = get_guidance(education, stream, interest)
    return render_template("result.html", name=name, guidance=guidance)

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    if "username" not in session:
        return redirect(url_for("login"))
    
    response = ""
    if request.method == "POST":
        user_message = request.form.get("message")
        response = generate_response(user_message)
    
    return render_template("chatbot.html", response=response)


# -------------------- RUN APP --------------------
if __name__ == "__main__":
    app.run(debug=True)
