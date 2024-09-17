from managers.book_manager import BookManager
from managers.user_manager import UserManager
from managers.checkout_manager import CheckoutManager
import logging

# Configure the logging
logging.basicConfig(
    filename='library_management.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)



def main_menu():
    """
    Display the main menu options and get user input.

    Returns:
        str: The user's choice from the menu options.
    """
    headline = "Library Management System"
    logging.info("Starting Library Management System.")
    print(f"\n{headline}\n{'=' * len(headline)}")

    print("1. Add User")
    print("2. Add Book")
    print("3. List Books")
    print("4. Checkout Book")
    print("5. Check-in Book")
    print("6. Exit \n")
    choice = input("Enter choice: ")
    print("\n")
    return choice

def main():
    """
    Main function to run the library management system.
    Initializes managers and handles user choices in a loop.
    """
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager()

    while True:
        choice = main_menu()
        if choice == '1':
            user_manager.add_user()
        elif choice == '2':
            book_manager.add_book()
        elif choice == '3':
            book_manager.list_books()
        elif choice == '4':
            user_id = input("Enter user ID: ")
            password = input("Enter password: ")
            if user_manager.authenticate_user(user_id, password):
                checkout_manager.checkout_book(user_id)
            else:
                logging.warning(f"Authentication failed for user {user_id}.")
                print("Authentication failed. Check your user ID or password.")
        elif choice == '5':
            checkout_manager.checkin_book()
        elif choice == '6':
            logging.info("Exiting Library Management System.")
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
