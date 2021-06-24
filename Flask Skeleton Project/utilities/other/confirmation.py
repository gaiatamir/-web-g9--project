# noinspection PyUnresolvedReferences
from app import mail
# noinspection PyUnresolvedReferences
from flask_mail import Mail, Message


# New Class for interact with DB
class Emails:
    def __init__(self):
        pass

    # New appointment
    def newAppointmentMail(self, email, username, DateT, service_type):
        subject = 'Appointment added successfully'
        message = Message(subject, sender="liranmor.r@gmail.com", recipients=["liranmor.r@gmail.com"])
        message.body = "name " + username + " email" + email + "DateTime " + DateT + "Type" + service_type
        mail.send(message)

        # New User

    def newUserMail(self, email, username):
        subject = 'Regisration completed successfully'
        message = Message(subject, sender="liranmor.r@gmail.com", recipients=[email])
        message.body = "name " + username + " email" + email
        mail.send(message)


# Creates an instance for the Emails class for export.
emails = Emails()
