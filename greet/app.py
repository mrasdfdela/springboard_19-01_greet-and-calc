from flask import Flask, request

app = Flask(__name__)

@app.route("/welcome")
def welcome():
  return "<h1>welcome</h1>"
  
@app.route("/welcome/<msg>")
def welcome_msg(msg):
  return f"<h1>welcome{' ' + msg}</h1>"