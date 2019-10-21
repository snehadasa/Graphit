#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.product import Product
from query_api.query_flipkart import query
import os
app = Flask(__name__)

@app_views.route('/search', methods=['GET'], strict_slashes=False)
def search_products():
    """Retrieves product from flipkart"""
    search_query = request.args['query']
    return jsonify(query(search_query)), 200


