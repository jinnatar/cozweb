#!/usr/bin/env python3

from flask import Flask
from cozify import hub, cloud

app = Flask(__name__)

@app.route("/")
def root():
    return "Index"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
