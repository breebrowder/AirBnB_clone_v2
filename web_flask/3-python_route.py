#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
    """ Method: return Hello """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Method: return HBNB """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """ Method: return C with value of text """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is cool"):
    """ Method: return Python with value of text """
    return "Python {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
