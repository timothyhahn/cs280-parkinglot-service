from flask import Flask
from settings import debug


app = Flask(__name__)


if debug:
    from flask.ext.admin import Admin
    from flask.ext.admin.contrib.sqlamodel import ModelView
    from models import ParkingLot
    from database import db_session
    admin = Admin(app)
    admin.add_view(ModelView(ParkingLot, db_session))


import parkinglot.views
