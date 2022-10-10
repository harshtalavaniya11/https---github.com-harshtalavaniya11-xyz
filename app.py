from flask import Flask
from pip import main
app=Flask(__name__)

@app.route("/")
def hello():
    return 'hello ddblogger'

@app.route("/homes")
def home():
    return 'home'

@app.route("/profile")
def profile():
    return "profile"

app.run(debug=True)