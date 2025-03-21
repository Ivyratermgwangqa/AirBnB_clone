#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The Place's ID (linked to Place.id).
        user_id (str): The User's ID (linked to User.id).
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
