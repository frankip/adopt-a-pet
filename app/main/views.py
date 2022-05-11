from flask import render_template,request,redirect,url_for
from . import main
from app.request import fetch_pets

# Views
@main.route('/')
def index():
    name = "Time to get started "
    
    pets = fetch_pets()
    
    print(f'----+++---{pets}')
    # context ={
    #     name: name
    # }
    return render_template('index.html', name=name, pets=pets)