from models.customer import Customer
from models.restaurant import  Restaurant
from models.review import  Review


def exit_program():
    print("Exiting the program...")
    exit()

def list_customers():
    try:
        # Get all customers from the database
        Customers = Customer.get_all()

        # Print each customers on a new line
        for customer in Customers:
            print(customer)

    except Exception as e:
        print(f"Error listing customers: {e}")

def list_restaurant():
    try:
        # Get all restaurants from the database
        restaurants = Restaurant.get_all()

        # Print each restaurants on a new line
        for restaurant in restaurants:
            print(restaurant)

    except Exception as e:
        print(f"Error listing restaurants: {e}")

def list_reviews():
    try:
        # Get all reviews from the database
        reviews = Review.get_all()

        # Print each reviews on a new line
        for review in reviews:
            print(review)

    except Exception as e:
        print(f"Error listing reviews: {e}")








