import re
from .basemodel import BaseModel
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = None
        self.is_admin = is_admin
        self.validate()

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def validate(self):
        """Validate user attributes"""
        if not (self.first_name and len(self.first_name) <= 50):
            raise ValueError("First name is required and must be less than or equal to 50 characters.")
        if not (self.last_name and len(self.last_name) <= 50):
            raise ValueError("Last name is required and must be less than or equal to 50 characters.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError("Invalid email format.")