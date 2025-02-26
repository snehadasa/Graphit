#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.product_page import *
from api.v1.views.search import *
