#!/usr/bin/python
""" holds class Product"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Customer(BaseModel, Base):
    """Representation of customers """
    __tablename__ = 'customers'
    name = Column(String(128), nullable=False)

    customer_id = Column(String(60), nullable=False)

    email_id = Column(String(128), nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes Product"""
        super().__init__(*args, **kwargs)

    @staticmethod
    def get_customer(customer_id):
        """ Gets Customer"""
        customers = models.storage.get_session().query(Customer).filter(Customer.customer_id == customer_id).all()
        if len(customers) > 0:
            return customers[0]
        else:
            return None