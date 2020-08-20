# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:21:02 2020

@author: Sankhasubhra Mandal
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()