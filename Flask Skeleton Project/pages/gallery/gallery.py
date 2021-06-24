from flask import Blueprint, render_template
# noinspection PyUnresolvedReferences
from utilities.other.DBint import DBint

# gallery blueprint definition
gallery = Blueprint('gallery', __name__, static_folder='static', static_url_path='/gallery.py',
                    template_folder='templates')


# Routes
@gallery.route('/gallery')
def index():
    GalleryImages = DBint.getImges()
    return render_template('gallery.html', GalleryImages=GalleryImages)
