from flask import render_template, request
from app import myobj

@myobj.route("/", methods =["GET", "POST"])
def home():
    name = 'Lisa'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    # if request.method == "POST":
    #     name = request.form.get("cname")
    #     return f'''<li>{name}</li>''' 
    return render_template('home.html', title='home', len = len(city_names), name = name, city_names=city_names, added = request.form.get("cname"))