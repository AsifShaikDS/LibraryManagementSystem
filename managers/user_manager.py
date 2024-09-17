from models.user import User
from storage.storage import Storage
import logging

class UserManager:
    def __init__(self):
        """
        Initialize the UserManager by loading existing user data from 'users.json'.
        """
        # Load existing users from the users.json file
        self.users = Storage.load_data("users.json")

    def user_exists(self, user_id):
        """
        Check if a user with the given user_id already exists.
        
        Args:
            user_id (str): The ID of the user to check for.
        
        Returns:
            bool: True if the user exists, False otherwise.
        """
        # Check if any user in the list has the same user_id
        exists = any(user.user_id == user_id for user in self.users)
        logging.debug(f"Checked existence of user with ID {user_id}: {exists}")
        return exists
    
    def add_user(self):
        """
        Add a new user to the system.
        Prompts the user for input and checks if the user ID already exists.
        """
        # Collect user details from the input
        user_id = input("Enter user ID: ").strip()
        # Check if the user ID already exists in the system
        if self.user_exists(user_id):
            logging.warning(f"Attempt to add a user with existing ID {user_id}.")
            print(f"User ID {user_id} already exists. Please use a different user ID.")
            return
        
        name = input("Enter user name: ").strip()
        password = input("Enter password: ").strip()

        # Ensure that none of the fields (name, user_id, password) are empty
        if not name or not user_id or not password:
            logging.error("All fields are required to add a user.")
            print("All fields are required. Please try again.")
            return

        self.users.append(User(name, user_id, password))
        self.save("users.json")
        print(f"User {name} added successfully.")

    def authenticate_user(self, user_id, password):
        """
        Authenticate the user by checking their user ID and password.
        
        Args:
            user_id (str): The ID of the user trying to log in.
            password (str): The password provided by the user.
        
        Returns:
            bool: True if the credentials match, False otherwise.
        """
        # Loop through all users to check if user_id and password match
        for user in self.users:
            if user.user_id == user_id and user.password == password:
                logging.info(f"User {user_id} authenticated successfully.")
                return True
        # If no match is found, return False
        return False

    def save(self, filename):
        """
        Save the updated user list to the specified file.
        
        Args:
            filename (str): The name of the file to save the data to.
        """
        # Save the user data to the specified file
        Storage.save_data(filename, self.users)
        logging.info(f"Users saved to {filename}.")
        print("User data saved successfully.")
