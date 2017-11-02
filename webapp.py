from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

if __name__ == '__main__':
    main()
    
@app.route("/")
def render_home():
     return render_template('counties.html')
def (counties):    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    state = []
    for c in counties:
        if not c["State"] in state:
            state.append(c["State"])
    print(state)    
