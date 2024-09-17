class Book:
    def __init__(self, title, author, isbn, is_checked_out=False):
        """
        Initialize a new Book object.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            is_checked_out (bool): A flag indicating whether the book is checked out. Defaults to False.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out

    def __str__(self):
        """
        Provide a string representation of the Book object.
        
        Returns:
            str: A string describing the Book's attributes.
        """
        return (f"Book(title={self.title}, author={self.author}, "
                f"isbn={self.isbn}, is_checked_out={self.is_checked_out})")
