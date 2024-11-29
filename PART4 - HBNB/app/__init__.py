from flask import Flask
from flask_restx import Api

from app.services.facade import HBnBFacade
facade = HBnBFacade()

from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt()

from flask_jwt_extended import JWTManager
jwt = JWTManager()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')


    from app.api.v1.users import api as users_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.reviews import api as reviews_ns

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    # Add bcrypt to the app, so that passwords will be encrypted.
    bcrypt.init_app(app)

    # Add jwt auth for the flask.
    jwt.init_app(app)

    return app