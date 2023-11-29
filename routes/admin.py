#!/usr/bin/python3
from routes import app_routes
from models.admin import Admin
from models import storage
from flask import jsonify, abort, request


@app_routes.route('admin_home')
def admin_home():
    return jsonify(message='Admin Home Page')


@app_routes.route('all_admins', methods=['GET'], strict_slashes=False)
def get_admins():
    admin_dict = storage.all('Admin').values()
    admin_list = [
        admin.to_dict()
        for admin in admin_dict
    ]
    return jsonify(admin_list)


@app_routes.route('/new_admin',
                  methods=['POST'],
                  strict_slashes=False)
def create_admin():
    if request.json is None:
        return 'Not a JSON', 400
    fields = request.get_json()
    if fields.get('username') is None:
        return 'Missing username', 400
    if fields.get('password') is None:
        return 'Missing password', 400
    admin = Admin(**fields)
    admin.save()
    return jsonify(admin.to_dict()), 201


@app_routes.route('delete_admin/<string:id>',
                  methods=['DELETE'],
                  strict_slashes=False)
def delete_admin_by_id(id):
    admin = storage.get('Admin', id)
    if admin is None:
        abort(404)
    admin.delete()
    storage.save()
    return jsonify({}), 200
