from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from app import facade
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

api = Namespace('places', description='Place operations')


# Models for input validation and output
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    @jwt_required()
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        current_user = get_jwt_identity()
        data = api.payload
        data['owner_id'] = current_user['id']
        place_data = api.payload
        try:
            new_place = facade.create_place(place_data)
            return {
                    "id": new_place.id,
                    "title": new_place.title,
                    "description": new_place.description,
                    "price": new_place.price,
                    "latitude": new_place.latitude,
                    "longitude": new_place.longitude,
                    "owner_id": new_place.owner_id
                    }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [
            {
                "id": place.id,
                "title": place.title,
                "description": place.description,
                "price": place.price,
                "latitude": place.latitude,
                "longitude": place.longitude,
                "owner_id": place.owner_id
            } for place in places
        ]

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        places_data = facade.get_place(place_id)
        if not places_data:
            return {'message': 'Place not found'}, 404
        return {
            "id": places_data.id,
            "title": places_data.title,
            "description": places_data.description,
            "price": places_data.price,
            "latitude": places_data.latitude,
            "longitude": places_data.longitude,
            "owner_id": places_data.owner_id
            }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        current_user = get_jwt_identity()
        place = facade.get_place(place_id)
        if not place:
            return {'message': 'Invalid input data'}, 400
        if place.owner_id != current_user['id']:
            return {'error': 'Unauthorized action'}, 403
        updated_data = api.payload
        updated_place = facade.update_place(place_id, updated_data)
        if not updated_place:
            return {'message': 'Place not found'}, 404
        
        return {
            "title": updated_place.title,
            "description": updated_place.description,
            "price": updated_place.price,
            "latitude": updated_place.latitude,
            "longitude": updated_place.longitude,
            "owner_id": updated_place.owner_id
            }, 200

@api.route('/places/<place_id>')
class AdminPlaceModify(Resource):
    @jwt_required()
    def put(self, place_id):
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)

        place_data = api.payload

        # Skip ownership check for admins
        if not is_admin:
            current_user_id = claims['id']
            place = facade.get_place(place_id)
            if place.owner_id != current_user_id:
                return {'error': 'Unauthorized action'}, 403

        # update the place
        updated_place = facade.update_place(place_id, place_data)
        return {
            "id": updated_place.id,
            "title": updated_place.title,
            "description": updated_place.description,
            "price": updated_place.price,
            "latitude": updated_place.latitude,
            "longitude": updated_place.longitude,
            "owner_id": updated_place.owner_id
            }, 200
