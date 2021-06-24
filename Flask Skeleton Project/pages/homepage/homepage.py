from flask import Blueprint, render_template, redirect, url_for
# noinspection PyUnresolvedReferences
from utilities.other.DBint import DBint

# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage.py',
                     template_folder='templates')


# Routes
@homepage.route('/')
def index():
    recommends = DBint.getRecommends()
    return render_template('Main.html', recommends=recommends)


@homepage.route('/homepage')
@homepage.route('/home')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
