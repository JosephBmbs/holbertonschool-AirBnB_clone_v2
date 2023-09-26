#!/usr/bin/python3

"""
Script for a Flask web application start
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function that displays "Hello HBNB!" """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbtnb():
    """ Function that displays HBNB """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def hbtnb1(text):
    """ Function that displays C followed by text """
    return "C {}".format(text.replace("_", " "))

@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def hbtnb2(text="is cool"):
    """ Function that displays Python followed by text """
    return "Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def hbtnb3(n):
    """ Function that displays n is a number only if n is a number """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def hbtnb5(n):
    """ Function that displays an HTML page """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
