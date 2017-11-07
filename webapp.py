from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)
@app.route("/")
def render_home():   
    return render_template('home.html',states=get_state_options())

def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    options = ""
    s = []
    for c in counties:
        if c["State"] not in s:
            s.append(c["State"])
        options += Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options
if __name__ == '__main__':
    app.run(debug=False, port=54321)
