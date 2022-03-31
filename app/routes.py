from flask import render_template, request
from app import myobj

name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myobj.route("/", methods =["GET", "POST"])
def home():
    # if request.method == "POST":
    #     name = request.form.get("cname")
    #     return f'''<li>{name}</li>''' 
    return render_template('home.html', title='home', len = len(city_names), name = name, city_names=city_names, added = request.form.get("cname"))