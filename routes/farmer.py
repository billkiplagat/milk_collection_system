#!/usr/bin/python3
from routes import app_routes
from models.farmer import Farmer
from models import storage
from flask import jsonify, abort, request


@app_routes.route('farmer_home')
def farmer_home():
    return jsonify(message='Farmer Home Page')


@app_routes.route('all_farmers', methods=['GET'], strict_slashes=False)
def get_farmers():
    farmers_dict = storage.all('Farmer').values()
    farmers_list = [
        farmers.to_dict()
        for farmers in farmers_dict
    ]
    return jsonify(farmers_list)


@app_routes.route('/new_farmer',
                  methods=['POST'],
                  strict_slashes=False)
def create_farmer():
    if request.json is None:
        return 'Not a JSON', 400
    fields = request.get_json()
    if fields.get('name') is None:
        return 'Missing name', 400
    if fields.get('contact_number') is None:
        return 'Missing contact_number', 400
    if fields.get('address') is None:
        return 'Missing address', 400
    if fields.get('password') is None:
        return 'Missing password', 400
    farmer = Farmer(**fields)
    farmer.save()
    return jsonify(farmer.to_dict()), 201


@app_routes.route('delete_farmer/<string:id>',
                  methods=['DELETE'],
                  strict_slashes=False)
def delete_farmer_by_id(id):
    farmer = storage.get('Farmer', id)
    if farmer is None:
        abort(404)
    farmer.delete()
    storage.save()
    return jsonify({}), 200
