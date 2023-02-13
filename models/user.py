#!/usr/bin/python3
"""Model for user"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class inheriting from BaseModel to manage User object"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
