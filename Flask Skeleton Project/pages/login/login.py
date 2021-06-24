from flask import Blueprint, render_template, request, session, redirect
# noinspection PyUnresolvedReferences
from utilities.other.forms import forms
# noinspection PyUnresolvedReferences
from utilities.other.confirmation import emails

# login blueprint definition
login = Blueprint('login', __name__, static_folder='static', static_url_path='/login.py', template_folder='templates')


# Routes

@login.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        useremail = request.form['email']
        userpass = request.form['Password']
        username = request.form['Name']
        if forms.registration(useremail, username, userpass) == 1:
            emails.newUserMail(useremail, username)
            massage = 'Registration succeeded!'
            return render_template('LogInRegister.html', massage=massage)
        success = False
    return render_template('LogInRegister.html', success=success)


@login.route('/login', methods=['GET', 'POST'])
def index():
    session['login'] = False
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['pass']
        if not forms.checkUserDet(email, passwd):
            massage = 'Email/password incorrect please try again!'
            return render_template('LogInRegister.html', massage=massage)
        session['login'] = True
        session['email'] = email
        return redirect('/')
    return render_template('LogInRegister.html')
