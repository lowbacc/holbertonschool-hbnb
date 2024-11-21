<p align="center">
  <img src="https://camo.githubusercontent.com/01adbf663e1e686f51890f18a45c82ec28d4843ca800e230e309ba4dd188b6d7/68747470733a2f2f6170706c792e686f6c626572746f6e7363686f6f6c2e636f6d2f686f6c626572746f6e2d6c6f676f2e706e67" alt="Logo Python" />
</p>

# HBnB Part 2 - BL and API - Implementation of Business Logic and API Endpoints

In this part of the HBnB Project, you will begin the implementation phase of the application based on the design developed in the previous part. The focus of this phase is to build the Presentation and Business Logic layers of the application using Python and Flask. You will implement the core functionality by defining the necessary classes, methods, and endpoints that will serve as the foundation for the application’s operation.

In this part, you will create the structure of the project, develop the classes that define the business logic, and implement the API endpoints. The goal is to bring the documented architecture to life by setting up the key functionalities, such as creating and managing users, places, reviews, and amenities, while adhering to best practices in API design.

It’s important to note that, at this stage, you will focus only on implementing the core functionality of the API. JWT authentication and role-based access control will be addressed in the next part. The services layer will be built using Flask and the flask-restx extension to create RESTful APIs.


## Objectives
By the end of this project, you should be able to:
- Set Up the Project Structure:

Organize the project into a modular architecture, following best practices for Python and Flask applications.
Create the necessary packages for the Presentation and Business Logic layers.

- Implement the Business Logic Layer:
Develop the core classes for the business logic, including User, Place, Review, and Amenity entities.
Implement relationships between entities and define how they interact within the application.
Implement the facade pattern to simplify communication between the Presentation and Business Logic layers.

- Build RESTful API Endpoints:
Implement the necessary API endpoints to handle CRUD operations for Users, Places, Reviews, and Amenities.
Use flask-restx to define and document the API, ensuring a clear and consistent structure.
Implement data serialization to return extended attributes for related objects. For example, when retrieving a Place, the API should include details such as the owner’s first_name, last_name, and relevant amenities.

- Test and Validate the API:
Ensure that each endpoint works correctly and handles edge cases appropriately.
Use tools like Postman or cURL to test your API endpoints.


## Project Vision and Scope
The implementation in this part is focused on creating a functional and scalable foundation for the application. You will be working on:

Presentation Layer: Defining the services and API endpoints using Flask and flask-restx. You’ll structure the endpoints logically, ensuring clear paths and parameters for each operation.

Business Logic Layer: Building the core models and logic that drive the application’s functionality. This includes defining relationships, handling data validation, and managing interactions between different components.

At this stage, you won’t need to worry about user authentication or access control. However, you should ensure that the code is modular and organized, making it easy to integrate these features in Part 3.



## Learning Objectives
This part of the project is designed to help you achieve the following learning outcomes:

Modular Design and Architecture: Learn how to structure a Python application using best practices for modularity and separation of concerns.
API Development with Flask and flask-restx: Gain hands-on experience in building RESTful APIs using Flask, focusing on creating well-documented and scalable endpoints.
Business Logic Implementation: Understand how to translate documented designs into working code, implementing core business logic in a structured and maintainable manner.
Data Serialization and Composition Handling: Practice returning extended attributes in API responses, handling nested and related data in a clear and efficient way.
Testing and Debugging: Develop skills in testing and validating APIs, ensuring that your endpoints handle requests correctly and return appropriate responses.


## Authors :
BENDAHMA Ibtissem : https://github.com/Tissem-Ben
LOWBACC Matthis : https://github.com/lowbacc
FERHAT Oussama : https://github.com/oussamafrt