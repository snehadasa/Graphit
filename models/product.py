#!/usr/bin/python
""" holds class Product"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Float, Index
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """Representation of city """
    __tablename__ = 'products'
    product_id = Column(String(60), nullable=False, index=True)
    price = Column(Float, nullable=False, default=0)
    product_id_index = Index('product_id_index', product_id);

    def __init__(self, *args, **kwargs):
        """initializes Product"""
        super().__init__(*args, **kwargs)
