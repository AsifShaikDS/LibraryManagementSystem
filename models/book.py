class Book:
    def __init__(self, title, author, isbn, is_checked_out=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out

    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, is_checked_out={self.is_checked_out})"
