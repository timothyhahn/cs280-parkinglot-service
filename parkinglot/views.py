from parkinglot import app
from flask import url_for, redirect, request, jsonify
from database import db_session
from models import ParkingLot
from helpers import distance_in_miles
from datetime import datetime


# API
## GET

@app.route('/lot', methods=['GET'])
def get_all_lots():
    lots = ParkingLot.query.all()
    lots_dict = dict()
    lots_list = list()
    for lot in lots:
        lots_list.append(lot.info())
    lots_dict['lots'] = lots_list
    return jsonify(lots_dict)

@app.route('/lot/distance')
def get_distance_lots():
    distance = (float)(request.args['distance'])
    latitude = (float)(request.args['latitude'])
    longitude = (float)(request.args['longitude'])
    lots = ParkingLot.query.all()
    lots_dict = dict()
    lots_list = list()
    for lot in lots:
        if distance_in_miles(latitude, longitude, lot.latitude, lot.longitude) <= distance:
            lots_list.append(lot.info())
    lots_dict['lots'] = lots_list
    return jsonify(lots_dict)
@app.route('/lot/<int:lot_id>', methods=['GET'])
def get_lot(lot_id):
    lot = ParkingLot.query.get(lot_id)
    if not lot:
        return jsonify(dict())
    return jsonify(lot.info())

@app.route('/lot', methods=['POST'])
def add_new_lot():
    name = request.form['name']
    pricing = request.form['pricing']
    hours = request.form['hours']
    longitude = request.form['longitude']
    latitude = request.form['latitude']

    lot = ParkingLot(name=name, pricing=pricing, hours=hours, longitude=longitude, latitude=latitude)
    db_session.add(lot)
    db_session.commit()
    return jsonify(lot.info())


@app.route('/lot/<int:lot_id>', methods=['POST'])
def edit_lot(lot_id):
    lot = ParkingLot.query.get(lot_id)
    if not lot:
        return jsonify(dict())

    lot.name = request.form['name']
    lot.pricing = request.form['pricing']
    lot.hours = request.form['hours']
    lot.longitude = request.form['longitude']
    lot.latitude = request.form['latitude']
    db_session.commit()
    return jsonify(lot.info())


@app.route('/lot/delete/<int:lot_id>', methods=['POST', 'DELETE'])
def delete_lot(lot_id):
    lot = ParkingLot.query.get(lot_id)
    if not lot:
        return jsonify(dict(status='Failed'))
    db_session.delete(lot)
    db_session.commit()
    return jsonify(dict(status='Success'))


# TURN OFF DB
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
