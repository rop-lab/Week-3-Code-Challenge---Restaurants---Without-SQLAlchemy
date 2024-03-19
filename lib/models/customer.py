from models.__init__ import CURSOR, CONN
from models.review import Review

class Customer:
    all = []
    
    def __init__(self, first_name, last_name, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        Customer.all.append(self)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
    def full_name(self):
        """Concatenate first name and last name"""
        return f"{self.first_name} {self.last_name}"
    
    def review_in_restaurant(self, restaurant):
        Review(self, restaurant)
        
    def reviews(self):
        return [review for review in Review.all if review.customer == self]
    
    def restaurants(self):
        return [review.restaurants for review in self.reviews()]
    
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS customers;"
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = "INSERT INTO customers (first_name, last_name) VALUES (?, ?)"
        CURSOR.execute(sql, (self.first_name, self.last_name))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all.append(self)
    
    @classmethod
    def create(cls, first_name, last_name):
        customer = cls(first_name, last_name)
        customer.save()
        return customer 
    
    def favorite_restaurant(self):
        reviews = self.reviews()
        if reviews:
            return max(reviews, key=lambda x: x.star_rating).restaurant

    def add_review(self, restaurant, star_rating):
        new_review = Review(self, restaurant, star_rating)
        new_review.save()

    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews() if review.restaurant == restaurant]
        for review in reviews_to_delete:
            review.delete()

    @classmethod
    def get_by_id(cls, id):
        sql = "SELECT * FROM customers WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        else:
            return None

    @classmethod
    def instance_from_db(cls, row):
        """Create and return a new Customer instance from database row"""
        return cls(row[1], row[2], row[0])  
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM customers"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
