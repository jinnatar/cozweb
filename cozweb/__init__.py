#!/usr/bin/env python3

__version__ = "0.0.1"

from absl import logging

from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object('websiteconfig')

from cozweb import devices
from cozify import hub

h = devices.CozifyDevices()

@app.route('/')
def root():
    logging.debug(h.rooms)
    return render_template('index.html', hubname=h.name, devices=h.devicecache, rooms=h.rooms)

@app.route('/device/<id>')
def device(id=None):
    d = hub.devices()
    return render_template('device.html', device=d[id])
    
@app.route('/device/<id>/toggle')
def device_toggle(id=None):
    hub.device_toggle(id)
    return "Done"
    
