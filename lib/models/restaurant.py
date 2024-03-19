from models.__init__ import CURSOR, CONN
from models.review import Review

class Restaurant:
    all = []

    def __init__(self, name, price, id=None):
        self.id = id
        self.name = name
        self.price = price
        Restaurant.all.append(self)
 
    def __str__(self):
        return f"{self.name} {self.price}"
    
    def reviews(self):
        return [review for review in Review.all if review.restaurant == self]

    def customers(self):
        return [review.customer for review in self.reviews()]

    def review_customer(self, customer):
        Review(customer, self)
        
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS restaurants;"
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO restaurants (name, price) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.price))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, price):
        restaurant = cls(name, price)
        restaurant.save()
        return restaurant 
    
    @classmethod
    def fanciest(cls):
        return max(cls.all, key=lambda x: x.price)

    def all_reviews(self):
        return [review.full_review() for review in self.reviews()]

    @classmethod
    def get_by_id(cls, id):
        sql = "SELECT * FROM restaurants WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        else:
            return None

    @classmethod
    def instance_from_db(cls, row):
        # Assuming the row contains (id, name, price) in order
        return cls(row[1], row[2], row[0])  # Create and return a new Restaurant instance
 
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM restaurants"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
