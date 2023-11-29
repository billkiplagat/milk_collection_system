#!/usr/bin/python3
""" Module for the main flask application """
from flask import Flask, jsonify
from models import storage
from os import getenv
from flask_cors import CORS
from routes import app_routes
from models.base_model import Base

app = Flask(__name__)

CORS(app, resources={"/*": {'origins': '0.0.0.0'}})

# Way to organize Flask application into smaller, reusable components.
app.register_blueprint(app_routes)

# Create the tables if they don't exist
Base.metadata.create_all(storage.get_engine())


@app.teardown_appcontext
def teardown(exception):
    """ closes the storage @app.teardown_appcontext is
         used to perform tasks that should be executed after
         each request to ensure proper resource
         management and prevent resource leaks"""
    storage.close()


@app.errorhandler(404)
def page_not_found(exception):
    """ Returns a JSON formatted 404 status code res"""
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    host = getenv("API_HOST")
    if host is None:
        host = '0.0.0.0'
    port = getenv("API_PORT")
    if port is None:
        port = 5000
    app.run(host=host, port=port, threaded=True)
