#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.product import Product
from models.customer import Customer
from models.customer_product_mapping import CustomerProductMapping
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Customer": Customer, "Product": Product,
           "CustomerProductMapping": CustomerProductMapping}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        GRAPHIT_MYSQL_USER = getenv('GRAPHIT_MYSQL_USER')
        GRAPHIT_MYSQL_PWD = getenv('GRAPHIT_MYSQL_PWD')
        GRAPHIT_MYSQL_HOST = getenv('GRAPHIT_MYSQL_HOST')
        GRAPHIT_MYSQL_DB = getenv('GRAPHIT_MYSQL_DB')
        GRAPHIT_ENV = getenv('GRAPHIT_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(GRAPHIT_MYSQL_USER,
                                             GRAPHIT_MYSQL_PWD,
                                             GRAPHIT_MYSQL_HOST,
                                             GRAPHIT_MYSQL_DB))

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """get object based on class and id"""
        objs = self.__session.query(classes[cls]).all()
        for obj in objs:
            if obj.__class__.__name__ == cls and obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        """get count of all objects or objects of a specific class"""
        object_count = 0
        object_list = []
        if cls is None:
            for value in classes.values():
                object_count += self.__session.query(value).count()
        else:
            if cls in classes:
                object_count += self.__session.query(classes[cls]).count()
        return object_count
