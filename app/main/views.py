from flask import render_template,request,redirect,url_for
from . import main
from app.request import fetch_pets, search_pets
from .forms import SearchForm

# Views
@main.route('/', methods=['GET', 'POST'])
def index():
    name = "Time to get started "
    form = SearchForm()
    pets = fetch_pets()
    
    if form.validate_on_submit():
        print(f'form list - {form.text.data}')
        search_results = search_pets(form.text.data)
        pets = search_results
        print(f'search rsult-----{pets[0].title}')
        return render_template('index.html', name=name, pets=pets, form=form)
    
    # print(f'----+++---{pets}')
    # context ={
    #     name: name
    # }
    return render_template('index.html', name=name, pets=pets, form=form)