import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)

# Exercise 1602: With these decorators (code that starts with @)
# we can define the URLS that the app listens to.


@app.route("/")
def index():
    # see comment in helper.py about getters and setters
    todos = helper.todos
    # Exercise 1602: Here we pass the data to the HTML
    # Normally this isn't possible, but flask will use this data
    # to generate new HTMLs to send to the client
    return render_template('index.html', todos=todos)


@app.route('/create/')
def add():
    title = request.args.get("title")
    print(title)
    helper.add(title)
    return redirect(url_for("index"))


@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))


# Exercise 1602: With these decorators (code that starts with @)
# we can define the URLS that the app listens to. Here we defined
# a new one!
@app.route('/secret')
def secret():
    return 42
