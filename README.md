# Week-3-Code-Challenge---Restaurants---Without-SQLAlchemy

## customer.py
-This Python code provides functionality for managing customers and their reviews in a restaurant management system. The system uses SQLite for data storage and provides various methods for interacting with customer data.

# Features
Customer Management: Create, retrieve, update, and delete customer profiles.
Review Management: Add, retrieve, and delete reviews made by customers for restaurants.
Database Operations: Create and drop database tables for storing customer information.

# Usage
1. Import the required modules:
`from models.__init__ import CURSOR, CONN`
`from models.review import Review`

2. Create a Customer object by providing first name and last name:
`customer = Customer.create("cheruiyot", "Rop")`

3. Add reviews for restaurants:
  `customer.review_in_restaurant(restaurant)`

 Retrieve reviews, favorite restaurants, and perform other operations using the defined methods.

# Code Structure

Customer Class: Represents a customer and provides methods for managing customer information and reviews.
__init__: Initializes a customer object with first name, last name, and optional id.
- full_name: Concatenates first name and last name.
- review_in_restaurant: Adds a review for a restaurant.
- reviews: Retrieves all reviews made by the customer.
- restaurants: Retrieves all restaurants reviewed by the customer.
- drop_table, create_table: Methods for managing the SQLite database table for customers.
- save, create: Methods for saving customer data to the database.
- favorite_restaurant: Retrieves the favorite restaurant based on reviews.
- add_review: Adds a new review for a restaurant.
- delete_reviews: Deletes reviews for a specific restaurant.
- get_by_id, instance_from_db, get_all: Methods for retrieving customer data from the database.

## restaurant.py
This file is used to define the Restaurant
- This Python code provides functionality for managing restaurants and their reviews in a restaurant review management system. The system uses SQLite for data storage and provides various methods for interacting with restaurant data.

# Features
- Restaurant Management: Create, retrieve, update, and delete restaurant profiles.
- Review Management: Add, retrieve, and delete reviews made for restaurants.
- Database Operations: Create and drop database tables for storing restaurant information.


# Usage
1. Import the required modules:
`from models.__init__ import CURSOR, CONN`
`from models.review import Review`
 2. Create a Restaurant object by providing the name and price:
 `restaurant = Restaurant.create("Restaurant Name", 50)`

 3. Add reviews for the restaurant:
`customer = Customer.create("Cheruiyot", "Rop")`
`restaurant.review_customer(customer)`

4. Retrieve reviews, customers, and perform other operations using the defined methods.

# Code Structure
* Restaurant Class: Represents a restaurant and provides methods for managing restaurant information and reviews.
__init__: Initializes a restaurant object with name, price, and optional id.
__str__: Returns a string representation of the restaurant.
- reviews: Retrieves all reviews made for the restaurant.
- customers: Retrieves all customers who reviewed the restaurant.
- review_customer: Adds a review for the restaurant by a customer.
- drop_table, create_table: Methods for managing the SQLite database table for restaurants.
- save, create: Methods for saving restaurant data to the database.
- fanciest: Retrieves the fanciest restaurant based on price.
- all_reviews: Retrieves all reviews for the restaurant.
- get_by_id, instance_from_db, get_all: Methods for retrieving restaurant data from the database.

## review.py
This Python code provides functionality for managing reviews in a review management system. It includes features to create, retrieve, and manage reviews for customers and restaurants. The system uses SQLite for data storage and provides various methods for interacting with review data.

# Usage

1. Import the module: `from models.
- The Review class inherits from this model.
- A Review can be created with attributes such as rating (integer), title (string), and body (string). It also has a method called ' 
- It has additional attributes such as rating and comment.
- The __init__ method initializes a review with these attributes plus an optional id.
- The __str__ method returns a string representation of the review.

# Code Structure

- The __init__ method initializes a review with these attributes plus an optional id.
- The __str__ method returns a string representation of the review.
- save: Saves the review to the database.
- get_by_id: Retrieves a review  from the database using its id.
- delete: Deletes a review from the database.
- instance_from_db: Creates an instance of the Review class from retrieved data from the database.
- get_all: Gets all reviews from the database.












