import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring1234"
messages = []


def add_messages(username, message):
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timesstamp": now, "from": username, "message": message}
    # messages.append("({}) {}: {}".format(now, username, message))
    messages.append(messages_dict)


@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instruction"""
    if request.method == "POST":
        session["username"] = request.form["username"]
    """if the username variable is is set, then instead of
     returning our index.html template, we're going to redirect
      to the contents of the session username variable."""
    if "username" in session:
        return redirect(session["username"])
    return render_template("index.html")


@app.route('/<username>')
def user(username):
    return render_template("chat.html", username=username, chat_messages=messages)


@app.route('/<username>/<message>')
def send_message(username, message):
    add_messages(username, message)
    return redirect("/" + username + message)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True, load_dotenv=True)