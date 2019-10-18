#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage

print("All objects: {}".format(storage.count()))
print("Product objects: {}".format(storage.count("Product")))

first_product_id = list(storage.all("Product").values())[0].id
print("First product: {}".format(storage.get("Product", first_product_id)))

