import pandas as pd
import requests
from user_simulator import UserSimulator
from flask import Flask, render_template, request

app = Flask(__name__)

recommender_endpoint = 'http://myrecsys1:5000/recommend'
feedback_endpoint = 'http://myfeedbackcollector1:5000/feedback'
simulator = UserSimulator('../data/user_activity.bz2', recommender_endpoint, feedback_endpoint)

@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        if request.form['mybutton'] == 'Start':
            simulator.start()
        elif request.form['mybutton'] == 'Stop':
            simulator.stop()
        else:
            pass
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

