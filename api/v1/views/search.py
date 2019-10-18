#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.product import Product
import os
app = Flask(__name__)

@app_views.route('/search', methods=['GET'], strict_slashes=False)
def get_products():
    """Retrieves product from flipkart"""
    query = request.get_json()['query']
    // result = search(query)
    // extract attributes
    // update database with price
    // return results


