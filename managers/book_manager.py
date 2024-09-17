from models.book import Book
from storage.storage import Storage
import logging

class BookManager:
    def __init__(self):
        """
        Initialize the BookManager by loading books from 'books.json'.
        """
        # Load the existing books data from the 'books.json' file
        self.books = Storage.load_data("books.json")

    def book_exists(self, isbn):
        """
        Check if a book with the given ISBN already exists.

        Args:
            isbn (str): The ISBN of the book to check.

        Returns:
            bool: True if the book exists, False otherwise.
        """
        # Use a generator expression to check if any book in the list has the same ISBN
        return any(book.isbn == isbn for book in self.books)
    
    def add_book(self):
        """
        Prompt the user for book details and add the book to the collection if it doesn't already exist.
        """
        # Gather the necessary book details from user input
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        isbn = input("Enter book ISBN: ").strip()

        # First, check if the book with the given ISBN already exists
        if self.book_exists(isbn):
            logging.warning(f"Attempt to add a book with existing ISBN {isbn}.")
            # If the ISBN exists, inform the user and stop the process
            print(f"A book with ISBN {isbn} already exists. Please use a different ISBN.")
            return
        
        # Ensure that all fields are provided, i.e., title, author, and ISBN
        if not title or not author or not isbn:
            logging.error("All fields are required to add a book.")
            print("All fields are required. Please try again.")
            return
        
        book = Book(title, author, isbn, False)
        self.books.append(book)
        # Save the updated list of books to the JSON file
        self.save("books.json")
        logging.info(f"Book '{title}' added successfully with ISBN {isbn}.")
        print(f"Book '{title}' added successfully.")

    def list_books(self):
        """
        List all the books in the collection.
        """
        # Loop through the list of books and print each one
        for book in self.books:
            print(book)
        logging.info("Listed all books.")

    def list_available_books(self):
        """
        Return a list of books that are currently available (i.e., not checked out).

        Returns:
            list: A list of books that are not checked out.
        """
        # Filter the list of books to only include those that are not checked out
        available_books = [book for book in self.books if not book.is_checked_out]
        logging.info("Listed available books.")
        return available_books

    def save(self, filename):
        """
        Save the current list of books to the specified file.

        Args:
            filename (str): The name of the file where the books will be saved.
        """
        # Save the books data to the JSON file using the Storage utility class
        Storage.save_data(filename, self.books)
        logging.info(f"Books saved to {filename}.")
