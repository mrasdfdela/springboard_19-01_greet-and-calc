from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operators = {'add': add, 'sub': sub, 'mult':mult, 'div': div}

@app.route('/<operator>')
def calculate(operator):
  var_a = int(request.args["a"])
  var_b = int(request.args["b"])

  if operator == 'add':
    return str(add(var_a,var_b))
  if operator == 'sub':
    return str(sub(var_a,var_b))
  if operator == 'mult':
    return str(mult(var_a,var_b))
  if operator == 'div':
    return str(div(var_a,var_b))
  else:
    return "<h1>Not a valid operator</h1>"


@app.route('/math/<operator>')
def calulate_math(operator):
  var_a = int(request.args["a"])
  var_b = int(request.args["b"])

  return str(operators[operator](var_a, var_b))