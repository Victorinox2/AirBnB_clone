#!/usr/bin/python3
""" Module for User class of an Air_bnb project """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class for Air_bnb project
    Attributes:
        email (str): user's email address
        password (str): user's password
        first_name (str): user's firstname
        last_name (str): user's last_name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
