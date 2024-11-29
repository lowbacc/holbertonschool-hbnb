# HBnB Flask API

## Overview

The HBnB Flask API is a modular, scalable web application following clear
separation of concerns through the Presentation, Business Logic, and Persistence
layers. This project is built using Flask and organized to accommodate future
integration of persistence mechanisms, such as a database-backed repository. The
current setup implements an in-memory repository to handle object storage and
validation, along with the Facade pattern to manage interaction between layers.

## Project Structure

```
part2/
├── app/
│   ├── __init__.py                   # Initializes the Flask app and API
│   ├── api/
│   │   ├── __init__.py               # Initializes API versioning
│   │   ├── v1/
│   │       ├── __init__.py           # Version 1 setup
│   │       ├── users.py              # User API endpoints
│   │       ├── places.py             # Place API endpoints
│   │       ├── reviews.py            # Review API endpoints
│   │       ├── amenities.py          # Amenity API endpoints
│   ├── models/
│   │   ├── __init__.py               # Initializes models package
│   │   ├── user.py                   # User model
│   │   ├── place.py                  # Place model
│   │   ├── review.py                 # Review model
│   │   ├── amenity.py                # Amenity model
│   ├── services/
│   │   ├── __init__.py               # Initializes services package
│   │   ├── facade.py                 # Implements the Facade pattern for business logic
│   ├── persistence/
│       ├── __init__.py               # Initializes persistence package
│       ├── repository.py             # In-memory repository for object storage
├── run.py                            # Entry point to start the Flask application
├── config.py                         # Configuration settings
├── requirements.txt                  # Lists dependencies
├── README.md                         # Project documentation
```

### Explaination of Key Directories and Files

* app/: Contains the main application components.
    
  * api/: Handles API routing and versioning.
  * models/: Defines business logic classes, like User, Place, Review, and Amenity.
  * services/: Implements the Facade pattern to act as a bridge between layers.
  * persistence/: Contains the in-memory repository, which will later be replaced by a database.

* run.py: Entry point for running the Flask application.
* config.py: Configuration settings for different environments.
* requirements.txt: Lists project dependencies for easy installation.
* README.md: Project documentation and setup instructions.


## Setup and Installation

### 1. Clone the Repository

```
git clone https://@github.com/SeasonofBeaver/holbertonschool-hbnb.git
cd holbertonschool-hbnb
```

### 2. Install Requirements

```
pip install -r requirements.txt
```

### 3. Run the Application

```
python run.py
```

This will start the Flask development server on ```http://127.0.0.1:5000/```.


## Future Enhancements

* Integrate a database-backed Persistence layer.
* Add error handling, input validation, and more complex business logic in future tasks.
* Expand test coverage with unit and integration tests.

## Authors

* [Quentin Lepoutre](https://github.com/MrKay12)
* [Jakob Stein](https://github.com/SeasonofBeaver)