#!/usr/bin/python3
""" Module for City class of the Air_bnb project """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class for an Air_bnb project
    Attributes:
        state_id(str): states's id
        name (str): city's firstname
    """

    state_id = ""
    name = ""
