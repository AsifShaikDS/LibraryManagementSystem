from models.book import Book
from storage.storage import Storage

class BookManager:
    def __init__(self):
        self.books = Storage.load_data("books.json")


    def book_exists(self, isbn):
        # Check if any book in the list has the same ISBN
        return any(book.isbn == isbn for book in self.books)
    
    def add_book(self):
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        isbn = input("Enter book ISBN: ").strip()

        # Check if the book with the given ISBN already exists
        if self.book_exists(isbn):
            print(f"A book with ISBN {isbn} already exists. Please use a different ISBN.")
            return
        
        if not title or not author or not isbn:
            print("All fields are required. Please try again.")
            return
        
        book = Book(title, author, isbn, False)
        self.books.append(book)
        self.save("books.json")
        # book_manager.add_item(title, author, isbn)
        print(f"Book '{title}' added successfully.")

    def list_books(self):
        for book in self.books:
            print(book)

    def list_available_books(self):
        available_books = [book for book in self.books if not book.is_checked_out]
        return available_books

    def save(self, filename):
        Storage.save_data(filename, self.books)
