from models.__init__ import CURSOR, CONN

class Review:
    all = []

    def __init__(self, customer_id, restaurant_id, star_rating, id=None):
        self.id = id
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.star_rating = star_rating
        Review.all.append(self)

        
    def _str_(self):
        return f"{self.customer_id} {self.restaurant_id} {self.star_rating}"
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS reviews;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS reviews (
        id INT PRIMARY KEY,
        customer_id INT,
        restaurant_id INT,
        star_rating INT,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
)
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql = """
            INSERT INTO reviews (customer_id, restaurant_id,star_rating)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.customer_id, self.restaurant_id,self.star_rating))
        CONN.commit()
        self.id = CURSOR.lastrowid
       # type(self).all[self.id] = self
    
    @classmethod
    def create(cls, customer_id, restaurant_id,star_rating):
        review = cls(customer_id, restaurant_id,star_rating)
        review.save()
        return review 
        
    def customer(self):
        from models.customer import  Customer
        return Customer.get_by_id(self.id)

    def restaurant(self):
        from models.restaurant import  Restaurant
        return Restaurant.get_by_id(self.id)

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."
    @classmethod
    def instance_from_db(cls, row):
        # Assuming the row contains (id, name, price) in order
        return cls(row[0], row[1], row[2], row[3])  # Create and return a new Customer instance

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM reviews"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]