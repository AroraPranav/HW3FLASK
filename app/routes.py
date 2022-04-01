#Discussed the homework problems with @BhagyeshRathi and @PranavPandey
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import flash, redirect, render_template
from app import myobj

name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

#Modified the code from the slides
class Submit(FlaskForm):
    city = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

#Some parts have modified code from the slides
@myobj.route("/", methods =["GET", "POST"])
def home():
    form = Submit()
    if form.validate_on_submit():
        flash(format(form.city.data))
        return redirect("/")
    return render_template('home.html', title='home',  
    name=name, city_names=city_names, form=form)