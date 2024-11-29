from .basemodel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.validate()

    def validate(self):
        if not (self.name and len(self.name) <= 50):
            raise ValueError("Amenity name is required and must be less than or equal to 50 characters.")