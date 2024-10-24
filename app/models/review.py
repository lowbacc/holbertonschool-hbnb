#!/usr/bin/python3


from .base_model import BaseModel
from place import Place
from user import User


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Review text is required and must be a string.")
        self.__text = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("Rating must be an integer between 1 and 5.")
        self.__rating = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if value is None or not isinstance(value, Place):
            raise ValueError("Place must be a valid Place instance.")
        self.__place = value

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        if value is None or not isinstance(value, User):
            raise ValueError("User must be a valid User instance.")
        self.__user = value
