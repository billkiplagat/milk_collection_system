#!/usr/bin/python3
from flask import Blueprint

app_routes = Blueprint("app_routes", __name__, url_prefix="/")

from routes.admin import *
from routes.farmer import *
from routes.milk_collection import *
from routes.reports import *
