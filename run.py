import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Main page with instruction"""
    return "To send a message use /Username/messsage"


@app.route('/<username>')
def user(username):
    return "Hi "+username


@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True, load_dotenv=True)