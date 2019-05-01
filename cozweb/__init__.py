#!/usr/bin/env python3

__version__ = "0.0.1"

from flask import Flask
app = Flask(__name__)
app.config.from_object('websiteconfig')

@app.route("/")
def root():
    return "Index"
