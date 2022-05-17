#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def time_now():
    now = datetime.now()

    date = str(now.strftime("%y/%m/%d"))
    time = str(now.strftime("%H:%M:%S"))
    
    return render_template('time.html', date=date, time=time)
