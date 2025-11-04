#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

#setup the basic routes
@app.route('/')
def index():
    return '<h1>This is the default route</h1>'

@app.route('/print/<string:parameter>')
def print_parameter(parameter):
    return f'<h1>The paramter is: {parameter}</h1>'

@app.route('/count/<int:number>')
def count_number(number):    
    output = ""
    for printval in range(number):
        output += f"The number is {printval}<br>\n"
    return f"{output}"

        

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '%':
        result = num1 / num2
    else:
        return '<h1>Invalid operation</h1>'

    return f'<h1>The result is: {result}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)


 
