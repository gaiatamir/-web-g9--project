from flask import Blueprint, render_template
# noinspection PyUnresolvedReferences
from utilities.other.DBint import DBint

# about blueprint definition
about = Blueprint('about', __name__, static_folder='static', static_url_path='/about.py', template_folder='templates')


# Routes
@about.route('/about')
def index():
    recommends = DBint.getRecommends()
    return render_template('AboutMe.html', recommends=recommends)
