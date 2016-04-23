"""

    Mange
    =====

    Management script for the Chiron application.

"""

from chiron.models import *
from flask_script import Manager
import datetime

from chiron import app, db

manager = Manager(app)


@manager.command
def run_debug():
    """
    Run the Chiron app in debug mode.
    """
    app.run(debug=True)


@manager.command
def initdb():
    """
    Setup the database
    """
    db.create_all()


@manager.command
def make_dummy_users():
    """
    Set the db up with dummy user stuff
    """
    dummyuser = User('Bob', 'iamanurse')
    db.session.add(dummyuser)
    db.session.commit()
    dummyrequest = LeaveRequest(1234, "Bob Smith", "0412345678", "I feel bad lol", date=datetime.date.today())
    dummyrequest2 = LeaveRequest(5678, "Tanda McHackathon", "01189998819991197253", "Can i like go fishing it's so nice out pls", date=datetime.date.today())
    db.session.add(dummyrequest)
    db.session.add(dummyrequest2)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
