from models.checkout import Checkout
from managers.book_manager import BookManager
from storage.storage import Storage
from datetime import datetime

class CheckoutManager:
    def __init__(self):
        self.checkouts = Storage.load_data("checkouts.json")
        self.book_manager = BookManager()

    def checkout_book(self, user_id):
        available_books = self.book_manager.list_available_books()
        if not available_books:
            print("No books are currently available for checkout.")
            return

        print("Available books:")
        for book in available_books:
            print(book)

        checkout_date = datetime.today().strftime('%Y-%m-%d')
        
        isbn = input("Enter ISBN of the book to check-in: ")

        for book in self.book_manager.books:
            if book.isbn == isbn and not book.is_checked_out:
                book.is_checked_out = True
                self.checkouts.append(Checkout(user_id, isbn, checkout_date))
                self.book_manager.save("books.json")
                Storage.save_data("checkouts.json", self.checkouts)
                print(f"Book {isbn} checked out by user {user_id}.")
                return
        print(f"Book {isbn} not available or doesn't exist.")

    def checkin_book(self):
        checked_out_books = self.list_checked_out_books()
        if not checked_out_books:
            print("No books are currently checked out.")
            return
        
        print("Checked-out books:")
        for book in checked_out_books:
            print(book)
        
        isbn = input("Enter ISBN of the book to check-in: ")
        
        for book in self.book_manager.books:
            if book.isbn == isbn and book.is_checked_out:
                book.is_checked_out = False
                self.checkouts = [co for co in self.checkouts if co.isbn != isbn]
                self.book_manager.save("books.json")
                Storage.save_data("checkouts.json", self.checkouts)
                print(f"Book {isbn} checked in.")
                return
        print(f"Book {isbn} was not checked out.")

    def list_checked_out_books(self):
        checked_out_books = [co for co in self.checkouts]
        return checked_out_books
