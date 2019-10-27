#!/usr/bin/python
""" holds class Product"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Float, Index
from datetime import datetime, timedelta
from sqlalchemy import cast, Date
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

    @staticmethod
    def get_product(product_id):
        """ Gets latest product that was queryied today"""
        current_time = datetime.utcnow()
        yesterday = current_time - timedelta(days=1)
        products = models.storage.get_session().query(Product).filter(Product.product_id == product_id).filter(
            Product.created_at > yesterday).all()
        if len(products) > 0:
            return products[0]
        else:
            return None

    @staticmethod
    def get_prices(product_id):
        """get price by date"""
        products = models.storage.get_session().query(Product).filter(Product.product_id == product_id).all()
        prices = {}
        for product in products:
            prices[product.created_at.strftime('%Y/%m/%d')] = product.price
        return prices

    @staticmethod
    def prices_range(product_id):
        """appending prices into array"""
        products = models.storage.get_session().query(Product).filter(Product.product_id == product_id).all()
        prices = []
        for product in products:
            prices.append(product.price)
        results = {}
        results['min_price'] = min(prices)
        results['max_price'] = max(prices)
        results['avg_price'] = sum(prices) / len(prices)
        return results