from flask import Blueprint, render_template, request, session
# noinspection PyUnresolvedReferences
from utilities.other.forms import forms
# noinspection PyUnresolvedReferences
from utilities.other.confirmation import emails

# appointments blueprint definition
appointments = Blueprint('appointments', __name__, static_folder='static', static_url_path='/appointments.py',
                         template_folder='templates')


# Routes
@appointments.route('/appointments')
def index():
    return render_template('Appointments.html')


@appointments.route('/newApp', methods=['GET', 'POST'])
def new_app():
    if request.method == 'POST':
        datet = request.form['cutDate']
        useremail = request.form['email']
        userp = request.form['Pnumber']
        username = request.form['Name']
        usercomm = request.form['Comments']
        service_type = request.form['service']
        if forms.insertAppointment(datet, username, userp, useremail, service_type, usercomm) == 1:
            massage = 'Appointment scheduled!'
            emails.newAppointmentMail(useremail, username, datet, service_type)
            return render_template('Main.html', massage=massage)
        success = False
    return render_template('Appointments.html', success=success)


@appointments.route('/deleteAppoint', methods=['GET', 'POST'])
def deleteAppoint():
    useremail1 = session.get('email')
    if request.form['email'] == useremail1:
        useremail = request.form['email']
        DTApp = request.form['cutDate']
        if DTApp == forms.checkUserDT(DTApp):
            forms.deleteApp(DTApp, useremail)
            massage = 'The appointment CANCELED'
            return render_template('Main.html', massage=massage)
    else:
        massage = 'Your not allowed to cancel this appointment'
        return render_template('Appointments.html', massage=massage)
