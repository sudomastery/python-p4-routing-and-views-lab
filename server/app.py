#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

#setup the basic routes
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_parameter(parameter):
    # Print to console and return the raw parameter text
    print(parameter)
    return parameter

@app.route('/count/<int:number>')
def count_number(number):    
    # Return numbers from 0 to number-1, each on its own line
    output = "\n".join(str(printval) for printval in range(number)) + "\n"
    return Response(output, mimetype='text/plain')

        

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    # Return plain text result
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


 
