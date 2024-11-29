from .basemodel import BaseModel
from app.models.place import Place
from app.models.user import User


class Review(BaseModel):
    def __init__(self, text, rating, user_id, place_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id

    def validate(self):
        if not self.text:
            raise ValueError("Review text is required.")
        if not (1 <= self.rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        if not isinstance(self.place, Place):
            raise ValueError("Place must be a valid Place instance.")
        if not isinstance(self.user, User):
            raise ValueError("User must be a valid User instance.")
