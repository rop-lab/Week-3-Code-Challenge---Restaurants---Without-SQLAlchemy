from models.__init__ import CURSOR, CONN
from models.review import Review

def get_all_reviews():
    """Retrieve all reviews in the database."""
    cursor = CURSOR(CONN)
    query = "SELECT * FROM review;"
    result = cursor.execute(query).fetchall()
    return [Review(*args) for args in result]

def add_new_review(product_id, user_id, rating, content):
    '''Add a new review to the database'''
    product_id = int(product_id)
    user_id = int(user_id)
    review = Review(None, product_id, user_id, rating, content)
    cursor = CURSOR(CONN)
    query = "INSERT INTO review (product_id, user_id, rating, content) VALUES(?,?,?,?)"
    cursor.execute(query, (review.product_id, review.user_id, review.rating, review.content))
    CONN.commit()
    return review 

def delete_a_review(review_id):
    '''Delete a specific review given its id'''
    review_id = int(review_id)
    cursor = CURSOR(CONN)
    query ="DELETE FROM review WHERE id=?"
    cursor.execute(query, (review_id,))
    CONN.commit()  

def search_reviews_by_keyword(keyword):
    '''Search for reviews containing a certain keyword'''
    # TODO: Implement this function
    pass
        
def search_reviews_in_range(minimum, maximum):
    '''Get all reviews with ratings within a range''' 
    min_val = float(minimum)
    max_val = float(maximum)
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    cursor = CURSOR(CONN)
    query = 'SELECT * FROM review WHERE rating BETWEEN ? AND ?'
    results = cursor.execute(query, (min_val, max_val)).fetchall()
    return [Review(*args) for args in results]

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
