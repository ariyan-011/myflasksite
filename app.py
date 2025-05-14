import sqlite3

def save_message(name, message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, name TEXT, message TEXT)')
    cursor.execute('INSERT INTO messages (name, message) VALUES (?, ?)', (name, message))
    conn.commit()
    conn.close()

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        save_message(name, message)
        return f"<h2>سلام {name}!</h2><p>پیامت ذخیره شد.</p>"
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

comments = []  # لیستی ساده برای ذخیره موقتی نظرات

@app.route("/comments", methods=["GET", "POST"])
def comments_page():
    if request.method == "POST":
        name = request.form["name"]
        text = request.form["text"]
        comments.append({"name": name, "text": text})
    return render_template("comments.html", comments=comments)

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)