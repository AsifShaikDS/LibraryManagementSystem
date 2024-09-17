from models.user import User
from storage.storage import Storage

class UserManager:
    def __init__(self):
        self.users = Storage.load_data("users.json")

    def user_exists(self, user_id):
        # Check if any user in the list has the same user_id
        return any(user.user_id == user_id for user in self.users)
    
    def add_user(self):
        user_id = input("Enter user ID: ").strip()
        name = input("Enter user name: ").strip()
        
        # Check if the user ID already exists
        if self.user_exists(user_id):
            print(f"User ID {user_id} already exists. Please use a different user ID.")
            return
        
        password = input("Enter password: ").strip()
        if not name or not user_id or not password:
            print("All fields are required. Please try again.")
            return
        self.users.append(User(name, user_id, password))
        # Storage.save_data("users.json", self.users)
        self.save("users.json")


    def authenticate_user(self, user_id, password):
        for user in self.users:
            if user.user_id == user_id and user.password == password:
                return True
        return False

    def save(self, filename):
        Storage.save_data(filename, self.users)
        print("User added successfully.")

