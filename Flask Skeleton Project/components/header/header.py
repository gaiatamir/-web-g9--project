from flask import Blueprint, render_template

# main_menu blueprint definition
header = Blueprint('header', __name__, static_folder='static', static_url_path='/header.py', template_folder='templates')
