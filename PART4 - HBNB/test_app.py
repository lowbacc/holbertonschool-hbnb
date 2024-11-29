import unittest
from app import create_app


class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user_success(self):
        """Test creating a user with valid data"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)

    def test_create_user_invalid_email(self):
        """Test creating a user with an invalid email format"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"), "Invalid input data")

    def test_create_user_missing_fields(self):
        """Test creating a user with missing required fields"""
        response = self.client.post('/api/v1/users/', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"), "Invalid input data")

    def test_get_user_not_found(self):
        """Test retrieving a non-existent user"""
        response = self.client.get('/api/v1/users/12345')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json.get("error"), "User not found")

class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_place_success(self):
        """Test creating a place with valid data"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Beautiful Beach House",
            "price": 200,
            "latitude": 40.7128,
            "longitude": -74.0060
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)

    def test_create_place_invalid_price(self):
        """Test creating a place with an invalid price (negative)"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Beautiful Beach House",
            "price": -50,
            "latitude": 40.7128,
            "longitude": -74.0060
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"), "Invalid input data")

    def test_create_place_out_of_range_coordinates(self):
        """Test creating a place with out-of-range latitude and longitude"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Remote Cabin",
            "price": 150,
            "latitude": 95.0,  # Invalid latitude
            "longitude": -200.0  # Invalid longitude
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"), "Invalid input data")

class TestReviewEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_review_success(self):
        """Test creating a review with valid data"""
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Amazing place to stay!",
            "user_id": "valid_user_id",
            "place_id": "valid_place_id"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)

    def test_create_review_empty_text(self):
        """Test creating a review with empty text"""
        response = self.client.post('/api/v1/reviews/', json={
            "text": "",
            "user_id": "valid_user_id",
            "place_id": "valid_place_id"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"), "Invalid input data")

    def test_create_review_invalid_user_place(self):
        """Test creating a review with non-existent user_id and place_id"""
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Amazing place to stay!",
            "user_id": "non_existent_user",
            "place_id": "non_existent_place"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"), "User or place not found")

class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity_success(self):
        """Test creating an amenity with valid data"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Swimming Pool"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)

    def test_create_amenity_empty_name(self):
        """Test creating an amenity with an empty name"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"), "Invalid input data")

    def test_get_amenity_not_found(self):
        """Test retrieving a non-existent amenity"""
        response = self.client.get('/api/v1/amenities/12345')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json.get("error"), "Amenity not found")

if __name__ == "__main__":
    unittest.main()
