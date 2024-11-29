from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from flask_bcrypt import Bcrypt
from sqlalchemy.orm.exc import NoResultFound

bcrypt = Bcrypt()

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

#User Facades
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)
    
    def get_all_user(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        for key, value in user_data.items():
            setattr(user, key, value)
        return user

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

#Amenity Facades
    def create_amenity(self, amenity_data):
        """Create a new amenity."""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Retrieve an amenity by ID."""
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """Retrieve all amenities."""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Update an amenity by ID."""
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            raise ValueError("Amenity not found.")

        for key, value in amenity_data.items():
            if hasattr(amenity, key):
                setattr(amenity, key, value)

        # Update the place in the repository
        self.place_repo.update(amenity_id, amenity.__dict__)  # Pass the dictionary of attributes

        return amenity
    
#Place Facade    
    def create_place(self, place_data):
    # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found.")
        return place

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        # Fetch the existing place
        existing_place = self.place_repo.get(place_id)
        if not existing_place:
            raise ValueError("Place not found.")

        # Update the existing place's attributes based on provided data
        for key, value in place_data.items():
            if hasattr(existing_place, key):
                setattr(existing_place, key, value)

        # Update the place in the repository
        self.place_repo.update(place_id, existing_place.__dict__)  # Pass the dictionary of attributes

        return existing_place
    
#Review Facade
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found.")
        return review

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):

        place = self.place_repo.get(place_id)
        if not place:
            return None
        return [review for review in self.review_repo.get_all() if review.place_id == place_id]

    def update_review(self, review_id, review_data):
        existing_review = self.review_repo.get(review_id)
        if not existing_review:
            raise ValueError("Review not found.")

        # Update the existing place's attributes based on provided data
        for key, value in review_data.items():
            if hasattr(existing_review, key):
                setattr(existing_review, key, value)
        
        self.review_repo.update(review_id, existing_review.__dict__)  # Pass the dictionary of attributes

        return existing_review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if review:
            self.review_repo.delete(review_id)
            return {'message': 'Review deleted sucessfully'}

    def has_user_reviewed_place(user_id, place_id):
        try:
            review = Review.query.filter_by(user_id=user_id, place_id=place_id).one_or_none()
            return review is not None
        except Exception as e:
            print(f"Error checking user review: {e}")
        return False