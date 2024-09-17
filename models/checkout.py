class Checkout:
    def __init__(self, user_id, isbn, checkout_date):
        self.user_id = user_id
        self.isbn = isbn
        self.checkout_date = checkout_date

    def __str__(self):
        return f"Checkout(user_id={self.user_id}, isbn={self.isbn}, checkout_date={self.checkout_date})"
