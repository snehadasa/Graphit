#!/usr/bin/python3
"""script that starts a Flask web application"""

import os
from flask import Flask, jsonify, render_template
from models import storage
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

@app.route('/product')
def product_page(the_id=None):
    """
    handles request to custom template for products
    """
    product_dict = storage.all(Product)
    result = product_dict.get("Product.{}".format(product_id))
    if result is not None:
        return render_template('1-hbnb.html', product=result)
    return "UNABLE TO SEARCH THE PRODUCT"

if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
