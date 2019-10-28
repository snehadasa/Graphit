#!/usr/bin/python3
""" console """

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models.product import Product
from models.customer import Customer
from models.customer_product_mapping import CustomerProductMapping
import shlex  # for splitting the line along spaces except in double quotes

classes = {"BaseModel": BaseModel,  "Product": Product, "Customer": Customer,
           "CustomerProductMapping": CustomerProductMapping}

CustomerProductMapping.update_prices()
