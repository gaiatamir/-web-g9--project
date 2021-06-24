from flask import Blueprint, render_template, request, session, flash
# noinspection PyUnresolvedReferences
from utilities.other.forms import forms

# login blueprint definition
account = Blueprint('account', __name__, static_folder='static', static_url_path='/account.py',
                    template_folder='templates')


# Routes
@account.route('/account', methods=['GET', 'POST'])
def index():
    useremail = session.get('email')
    if request.method == 'POST':
        passw = request.form['pass']
        newpasswd = request.form['newpass']
        newpasswd1 = request.form['newpass1']
        if forms.checkPass(useremail, passw, newpasswd, newpasswd1):
            forms.changePass(useremail, newpasswd)
            massage = 'Your password updated!'
            return render_template('account.html', userEmail=useremail, massage=massage)
        else:
            massage = 'One of the details incorrect!'
            return render_template('account.html', userEmail=useremail, massage=massage)
    return render_template('account.html', userEmail=useremail)


@account.route('/deleteAccount', methods=['GET', 'POST'])
def deleteAccount():
    useremail = session.get('email')
    if request.form['userEmail'] == useremail:
        forms.deleteAccount(useremail)
        session['login'] = False
        massage = 'Delete successfully!'
        return render_template('Main.html', massage=massage)
    alert = 'Your not allowed to delete another account, try again!'
    return render_template('account.html', massage=alert)


@account.route('/addRecommend', methods=['GET', 'POST'])
def addRecommend():
    if request.method == 'POST':
        name = request.form['name']
        recommend = request.form['recommend']
        forms.insertRecommend(name, recommend)
        massage = 'Added successfully!'
        return render_template('account.html', massage=massage)
    return render_template('Main.html')
