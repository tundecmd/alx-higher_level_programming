#!/usr/bin/python3
"""
Contains the class definition of a City and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    Class representing the cities table

    Attributes:
        __tablename__ (str): The table name of the class
        id (sqlalchemy.Integer): The id of the city
        name (sqlalchemy.String): The name of the city
        state_id (sqlalchemy.Column): The city's state id
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
