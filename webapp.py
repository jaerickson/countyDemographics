from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

def get_state_options():
    with open('county_demographics.json') as demographics_data:
        state = json.load(demographics_data)
    options = ""
    currentState = state[0]["State"]
    for c in state:
        if c["State"] != currentState:
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    return options
@app.route("/")
def render_home():   
    return render_template('home.html',states=get_state_options())
if __name__ == '__main__':
    app.run(debug=False, port=54321)
