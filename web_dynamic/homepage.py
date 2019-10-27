#!/usr/bin/python3
"""script that starts a Flask web application"""

import os
from flask import Flask, jsonify, render_template, request
from models import storage
from models.customer import Customer
from models.customer_product_mapping import CustomerProductMapping
from query_api.query_flipkart import query, query_product
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
    return render_template('homepage.html', items=[])


@app.route('/search')
def search_products():
    """
    searches product.
    """
    search_query = request.args['query']
    if not search_query:
        return render_template('homepage.html', items=[]);
    items = query(search_query)
    return render_template('homepage.html', items=items)
    #return jsonify(items), 200


@app.route('/create_customer_mapping')
def create_customer_mapping():
    """ Creates customer mapping"""
    customer_id = request.args['customer_id']
    product_id = request.args['product_id']
    if not customer_id or not product_id:
        return jsonify({"error": "Not found"}), 404
    customer = Customer.get_customer(customer_id)
    if not customer:
        args = {'customer_id': customer_id, 'email_id': customer_id, 'name': customer_id}
        customer = Customer(**args)
        customer.save()
    customer_product = CustomerProductMapping.get_customer_product(customer_id, product_id)
    # product_mapper = CustomerProductMapping.get_customer_product(product_id)
    if not customer_product:
        kwargs = {'customer_id': customer_id, 'product_id': product_id}
        customer_product = CustomerProductMapping(**kwargs)
        customer_product.save()
    return jsonify({}), 200

@app.route('/customers')
def customer_products():
    """get product id based on customers"""
    customer_id = request.args['customer_id']
    customers = Customer.get_customer(customer_id)
    if not customer_id or not customers:
        return render_template('homepage.html', items=[])
    products = []
    for customer_product in CustomerProductMapping.get_customer_mappings(customer_id):
        product = query_product(customer_product.product_id)
        if product is not None:
            products.append(product)
    return render_template('homepage.html', items=products)


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
