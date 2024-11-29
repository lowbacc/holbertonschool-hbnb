from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from app import facade
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt


api = Namespace('reviews', description='Review operations')



review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @jwt_required()
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        current_user = get_jwt_identity()
        review_data = api.payload
        if ('text' not in review_data or 'rating' not in review_data or
                'user_id' not in review_data or 'place_id' not in review_data):
            return {'message': 'Missing required fields'}, 400
        place = facade.get_place(review_data['place_id'])
        if place.owner_id == current_user['id']:
            return {'error': 'You cannot review your own place'}, 400

        if facade.has_user_reviewed_place(current_user['id'], review_data['place_id']):
            return {'error': 'You have already reviewed this place'}, 400
        review_data['user_id'] = current_user['id']

        new_review = facade.create_review(review_data)
        return {
                'id': new_review.id,
                'text': new_review.text,
                'rating': new_review.rating,
                'user_id': new_review.user_id,
                'place_id': new_review.place_id
            }, 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return [
            {
                'id': review.id,
                'text': review.text,
                'rating': review.rating,
                'user_id': review.user_id,
                'place_id': review.place_id
            } for review in reviews
        ], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        print("Review retrieved:", review)
        return {
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user_id': review.user_id,
            'place_id': review.place_id
        }, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, review_id):
        """Update a review's information"""
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        if review.user_id != current_user['id']:
            return {'error': 'Unauthorized action'}, 403
        review_data = api.payload

        updated_review = facade.update_review(review_id, review_data)
        return {
            'id': updated_review.id,
            'text': updated_review.text,
            'rating': updated_review.rating,
            'user_id': updated_review.user_id,
            'place_id': updated_review.place_id
        }, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)
        if review.user_id != current_user['id']:
            return {'error': 'Unauthorized action'}, 403
        success = facade.delete_review(review_id)
        if success:
            return {'message': 'Review deleted successfully'}, 200
        else:
            return {'error': 'Review not found'}, 404

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        place_reviews = facade.get_reviews_by_place(place_id)
        if not place_reviews:
            return {'error': 'Place not found'}, 404
        return [
            {
                'id': review.id,
                'text': review.text,
                'rating': review.rating
            } for review in place_reviews
        ], 200

@api.route('/reviews/<review_id>')
class AdminReviewModify(Resource):
    @jwt_required()
    def put(self, review_id):
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)

        review_data = api.payload

        # Skip ownership check for admins
        if not is_admin:
            current_user_id = claims['id']
            review = facade.get_review(review_id)
            if review.user_id != current_user_id:
                return {'error': 'Unauthorized action'}, 403

        # Logic to update the review
        updated_review = facade.update_review(review_id, review_data)
        return {
            'id': updated_review.id,
            'text': updated_review.text,
            'rating': updated_review.rating,
            'user_id': updated_review.user_id,
            'place_id': updated_review.place_id
        }, 200
