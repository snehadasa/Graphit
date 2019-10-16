#!/usr/bin/python3
"""This is the CustomerProductMapping class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from sqlalchemy import DateTime


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
