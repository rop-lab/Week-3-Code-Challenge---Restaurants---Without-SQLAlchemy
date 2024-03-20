from models.customer import  Customer
from models.restaurant import  Restaurant
from models.review import  Review


def seed_database():
    
    Customer.drop_table() 
    Restaurant.drop_table()
    Review.drop_table()
    Customer.create_table()
    Restaurant.create_table()
    Review.create_table()

# #seeding customer table
    Customer.create("Dennis", "Kipkirui")
    Customer.create("Cheruiyot","Rop")
#seeding restaurants
    Restaurant.create("The Pizza Place", 2)
    Restaurant.create("The Dawn", 3)
#seeding reviews
    Review.create(1, 1, 5)

seed_database()
print("success")


