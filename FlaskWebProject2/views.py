"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject2 import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
app.config['SECRET_KEY'] = 'The first argument to the field'
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/PhotoAlbum')
def PhotoAlbum():
    """Renders the about page."""
    return render_template(
        'PhotoAlbum.html',
        title='PhotoAlbum',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/Query')
def Query():
    print("Running from()")
    name = None
    capital = ''
    form = CountryForm()
    df = pd.read_csv('capitals.csv')
    df = df.set_index('Country')
    if form.validate_on_submit():
        name = form.name.data
        if name in df.index:
            capital - df.loc[name , 'Capital']
        else: 
            capital = name + ', no such country'
            form.name.data = ''
    return render_template('Query.html' , form=form, name=capital,raw_data_table=df.to_html(classes = 'table table-hover')
        
    )
class CountryForm(FlaskForm):
    name = StringField('Country Name?)' , validators = [DataRequired()])
    submit = SubmitField('Submit')
    # change
    # change