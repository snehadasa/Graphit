#!/usr/bin/python3
"""This is the CustomerProductMapping class"""
from models.base_model import BaseModel, Base
from models.product import Product
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from query_api.query_flipkart import query_product
from os import getenv
from sqlalchemy import DateTime
import models


class CustomerProductMapping(BaseModel, Base):
    """This is the class for for CustomerproductsMapping
    """

    __tablename__ = 'customers_products'

    product_id = Column(String(60),
                        ForeignKey('products.product_id'),
                        nullable=False)

    customer_id = Column(String(60),
                         ForeignKey('customers.customer_id'),
                         nullable=False)

    customer = relationship("Customer",
                            backref="customers_products")

    products = relationship("Product",
                            backref="customers_products")


    @staticmethod
    def get_customer_product(customer_id, product_id):
        """this is a customer product mapper"""
        customers_products = models.storage.get_session().query(CustomerProductMapping).filter(
            CustomerProductMapping.customer_id == customer_id).filter(
            CustomerProductMapping.product_id == product_id).all()
        if len(customers_products) > 0:
            return customers_products[0]
        else:
            return None

    @staticmethod
    def get_customer_mappings(customer_id):
        """get all the products related to that customer"""
        return models.storage.get_session().query(CustomerProductMapping).filter(
            CustomerProductMapping.customer_id == customer_id).all()

    @staticmethod
    def update_prices():
        """Update prices of all customer"""
        customer_product_mappings = models.storage.get_session().query(CustomerProductMapping).all()
        product_ids = {}
        for customer_product_mapping in customer_product_mappings:
            product_id = customer_product_mapping.product_id
            if product_id not in product_ids.keys():
                print(product_id)
                product_ids[product_id] = True
                product = Product.get_product(product_id)
                if not product:
                    query_product(product_id)