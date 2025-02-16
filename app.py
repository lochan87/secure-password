from flask import Flask, render_template, request, redirect, url_for, flash
from db import save_password, get_password, init_db, save_master, get_master

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Initialize database
init_db()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

def content():
    return render_template("content.html")

@app.route("/create_master", methods=["POST"])
def create_master():
    name = request.form.get("name")
    username = request.form.get("username")
    master_password = request.form.get("master_password")
    con_master_password = request.form.get("con_master_password")
    if master_password == con_master_password and master_password:
        save_master(username, name, master_password)
        flash("Master password set successfully!", "success")
    else:
        flash("Master password cannot be empty!", "danger")

    return redirect(url_for("home"))

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    master_password = request.form.get("master_password")
    result = get_master(username)

    if result and master_password == result[1]:
        flash("Login successful!", "success")
        return content()
    else:
        flash("Invalid master password!", "danger")
    return redirect(url_for("home"))

# ✅ Route to Add Password
@app.route("/add", methods=["POST"])
def add_password():
    website = request.form.get("website")
    username = request.form.get("username")
    password = request.form.get("password")

    if website and username and password:
        save_password(website, username, password)
        flash("Password saved successfully!", "success")
    else:
        flash("All fields are required!", "danger")

    return redirect(url_for("content"))

# ✅ Route to Retrieve Password
@app.route("/retrieve", methods=["POST"])
def retrieve_password():
    website = request.form.get("website")
    result = get_password(website)

    if result:
        username, password = result
        flash(f"Username: {username} | Password: {password}", "info")
    else:
        flash("No password found for this website.", "danger")

    return content()

if __name__ == "__main__":
    app.run(debug=True)

