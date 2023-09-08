from flask import Flask, Response, redirect, render_template, request, url_for

import helper

app = Flask(__name__)


@app.route("/")
def index():
    todos = helper.get_all()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("text")
    date = request.form.get("date")
    category = request.form.get("category")
    description = request.form.get("description")
    helper.add(title, date, category, description)
    return redirect(url_for("index"))


@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(url_for("index"))
