#!/usr/bin/python3
"""script that starts a Flask web application"""

import os
from flask import Flask, jsonify, render_template, request
from models import storage
from query_api.query_flipkart import query
import uuid

# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()

@app.route('/')
def graphit_homepage():
    """
    handles request for homepage
    """
    return render_template('homepage.html')

@app.route('/search')
def search_products():
    """
    searches product.
    """
    search_query = request.args['query']
    if not search_query:
        return render_template('homepage.html');
    items = query(search_query)
    return render_template('product.html', items=items)


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
