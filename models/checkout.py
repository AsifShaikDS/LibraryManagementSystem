class Checkout:
    def __init__(self, user_id, isbn, checkout_date):
        """
        Initialize a new Checkout object.

        Args:
            user_id (str): The ID of the user who checked out the book.
            isbn (str): The ISBN of the book being checked out.
            checkout_date (str): The date when the book was checked out (in 'YYYY-MM-DD' format).
        """
        self.user_id = user_id
        self.isbn = isbn
        self.checkout_date = checkout_date

    def __str__(self):
        """
        Provide a string representation of the Checkout object.

        Returns:
            str: A string describing the Checkout's attributes, including user ID, book ISBN, and checkout date.
        """
        return (f"Checkout(user_id={self.user_id}, isbn={self.isbn}, "
                f"checkout_date={self.checkout_date})")
