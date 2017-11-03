from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)
    
@app.route("/")
def render_home():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('counties.html',options=)
def get_state_options(counties):    
    s = []
    for c in counties:
        if not c["State"] in s:
            state.append(c["State"])
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") 
    return options
if __name__ == '__main__':
    app.run(debug=False, port=54321)
