from models.checkout import Checkout
from managers.book_manager import BookManager
from storage.storage import Storage
from datetime import datetime
import logging

class CheckoutManager:
    def __init__(self):
        """
        Initialize the CheckoutManager by loading checkouts and setting up the BookManager.
        """
        # Load existing checkout data from 'checkouts.json'
        self.checkouts = Storage.load_data("checkouts.json")
        # Initialize the BookManager to manage book-related tasks
        self.book_manager = BookManager()

    def checkout_book(self, user_id):
        """
        Allow a user to check out a book if it's available.

        Args:
            user_id (str): The ID of the user checking out the book.
        """
        # Get the list of available books (i.e., not checked out)
        available_books = self.book_manager.list_available_books()
        
        # If there are no books available for checkout, notify the user and return
        if not available_books:
            print("No books are currently available for checkout.")
            return

        # Display the list of available books
        print("Available books:")
        for book in available_books:
            print(book)

        # Get the current date for the checkout record
        checkout_date = datetime.today().strftime('%Y-%m-%d')
        
        # Prompt the user to enter the ISBN of the book they wish to check out
        isbn = input("Enter ISBN of the book to check out: ")

        # Search for the book in the collection
        for book in self.book_manager.books:
            # If the book is found and it is available for checkout
            if book.isbn == isbn and not book.is_checked_out:
                # Mark the book as checked out
                book.is_checked_out = True
                # Add a new checkout entry with the user ID and checkout date
                self.checkouts.append(Checkout(user_id, isbn, checkout_date))
                # Save the updated book list and checkout data
                self.book_manager.save("books.json")
                Storage.save_data("checkouts.json", self.checkouts)
                # Confirm to the user that the book has been checked out
                print(f"Book {isbn} checked out by user {user_id}.")
                logging.info(f"Book {isbn} checked out by user {user_id}.")
                return
        
        # If the book is not available or doesn't exist, notify the user
        print(f"Book {isbn} not available or doesn't exist.")

    def checkin_book(self):
        """
        Allow a user to check in (return) a book.

        The book must have been checked out first.
        """
        # Get the list of books currently checked out
        checked_out_books = self.list_checked_out_books()
        
        # If there are no books checked out, notify the user and return
        if not checked_out_books:
            print("No books are currently checked out.")
            return
        
        # Display the list of checked-out books
        print("Checked-out books:")
        print(checked_out_books)
        
        # Prompt the user to enter the ISBN of the book they wish to check in
        isbn = input("Enter ISBN of the book to check in: ")
        
        # Search for the book in the collection
        for book in self.book_manager.books:
            # If the book is found and is currently checked out
            if book.isbn == isbn and book.is_checked_out:
                book.is_checked_out = False
                self.checkouts = [co for co in self.checkouts if co.isbn != isbn]
                # Save the updated book list and checkout data
                self.book_manager.save("books.json")
                Storage.save_data("checkouts.json", self.checkouts)
                print(f"Book {isbn} checked in.")
                logging.info(f"Book {isbn} checked in.")
                
                return
        logging.error(f"Book {isbn} was not checked out.")
        # If the book was not checked out or doesn't exist, notify the user
        print(f"Book {isbn} was not checked out.")

    def list_checked_out_books(self):
        """
        List all books that are currently checked out.

        Returns:
            list: A list of checkout objects representing books that are checked out.
        """
        # Simply return the list of all checked-out books
        checked_out_books = [co for co in self.checkouts]
        return checked_out_books
