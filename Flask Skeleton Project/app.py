from flask import Flask, render_template

# noinspection PyUnresolvedReferences
from flask_mail import Mail, Message

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')
mail= Mail(app)
#
#Mail settings
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'liranmor.r@gmail.com'
app.config['MAIL_PASSWORD'] = 'liran2506'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## login
from pages.login.login import login
app.register_blueprint(login)

## About
from pages.about.about import about
app.register_blueprint(about)

## gallery
from pages.gallery.gallery import gallery
app.register_blueprint(gallery)

## appointments
from pages.appointments.appointments import appointments
app.register_blueprint(appointments)

## account
from pages.account.account import account
app.register_blueprint(account)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu

from components.footer.footer import footer
app.register_blueprint(footer)


from components.header.header import header
app.register_blueprint(header)


if __name__ == '__main__':
    app.run(debug=True)