# noinspection PyUnresolvedReferences
from utilities.db.db_manager import dbManager


# New Forms Class for interact with DB

class Forms:
    def __init__(self):
        pass

        # Registration New User

    def registration(self, useremail, username, userpass):
        query = "INSERT INTO users (email,name ,password) VALUES ('%s','%s', '%s')" % (
            useremail, username, userpass)
        dbManager.commit(query)
        return True

    # Login Page - Check User in DB
    def checkUserDet(self, email, passw):
        return dbManager.fetch(f"Select * From users WHERE email='{email}' AND password='{passw}'")

    # Set - Update new password for user
    def changePass(self, email, newpass):
        query = "UPDATE users SET password = '%s' WHERE email='%s'" % (newpass, email)
        dbManager.commit(query)
        return True

    def checkPass(self, email, passwd, newpasswd, newpasswd1):
        if not self.checkUserDet(email, passwd):
            return False
        elif newpasswd == newpasswd1:
            return True

        # Delete user from DB

    def deleteAccount(self, email):
        query = "DELETE FROM users WHERE email='%s'" % email
        dbManager.commit(query)
        return True

    # new appointment
    def insertAppointment(self, DateT, username, phonenumber, useremail, service_type, usercomment):
        query = "INSERT INTO appointments (DT,name, phone, email, service_type, comment) VALUES ('%s','%s', '%s','%s','%s','%s')" % \
                (DateT, username, phonenumber, useremail, service_type, usercomment)
        dbManager.commit(query)
        return True

    def deleteApp(self, DateT, email):
        query = "DELETE FROM appointments WHERE email='%s' AND DT='%s'" % (email, DateT)
        dbManager.commit(query)
        return True

    # Creates an instance for the forms class for export

    # Login Page - Check User in DB
    def checkUserDT(self, DateT):
        return dbManager.fetch(f"Select * From appointments WHERE DT='%s'" % DateT)

    # new recommend
    def insertRecommend(self, name, recommend):
        query = "INSERT INTO recommends (name, details) VALUES ('%s','%s')" % \
                (name, recommend)
        dbManager.commit(query)
        return True


forms = Forms()
