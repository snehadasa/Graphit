#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.product import Product
import os
app = Flask(__name__)


@app_views.route('/products', methods=['GET'], strict_slashes=False)
def get_products():
    """Retrieves the list of all Product objects"""
    products = storage.all('Product')
    product_list = []
    for product in products.values():
        product_list.append(product.to_dict())
    return jsonify(product_list), 200


@app_views.route('/products/<product_id>', methods=['GET'], strict_slashes=False)
def get_product(product_id=None):
    """Retrieves a Product object with the id linked to it"""
    product_dict = storage.all('Product')
    product = product_dict.get('Product' + "." + product_id)
    if product is None:
        abort(404)
    else:
        return jsonify(product.to_dict()), 200


@app_views.route('/products/<product_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_product(product_id=None):
    """Deletes a State object"""
    obj = storage.get('Product', product_id)
    if obj is None:
        abort(404)
    else:
        storage.delete(obj)
        storage.save()
    return jsonify({}), 200


@app_views.route('/products', methods=['POST'], strict_slashes=False)
def post_product():
    """Creates product"""
    result = request.get_json()
    if not result:
        abort(400, {"Not a JSON"})
    if 'name' not in result:
        abort(400, {"Missing name"})
    obj = Product(name=result['name'])
    storage.new(obj)
    storage.save()
    return jsonify(obj.to_dict()), 201


@app_views.route('/products/<product_id>', methods=['PUT'], strict_slashes=False)
def put_product(product_id=None):
    """Updates a Product object"""
    result = request.get_json()
    if not result:
        abort(400, {"Not a JSON"})
    obj = storage.get('Product', state_id)
    if obj is None:
        abort(404)
    invalid_keys = ["id", "created_at", "updated_at"]
    for key, value in result.items():
        if key not in invalid_keys:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict()), 200
