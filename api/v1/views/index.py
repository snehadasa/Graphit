#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from models.product import Product
from models.base_model import BaseModel
from models.customer import Customer

app = Flask(__name__)


@app_views.route('/status')
def status():
    return jsonify({
                     "status": "OK"
                   })


@app_views.route('/stats')
def stat():
    class_dict = {"products": "Product"}
    for key in class_dict:
        class_dict[key] = storage.count(class_dict[key])
    return jsonify(class_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
