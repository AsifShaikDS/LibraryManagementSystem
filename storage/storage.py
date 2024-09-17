import json
from models.book import Book
from models.checkout import Checkout
from models.user import User

class Storage:
    @staticmethod
    def save_data(filename, data):
        """
        Save the list of objects to a file in JSON format.

        Args:
            filename (str): The file to which the data will be saved.
            data (list): A list of objects that will be serialized and saved.
        """
        # Open the file in write mode and dump the list of objects as JSON
        with open(filename, 'w') as file:
            # We convert each object in the list to a dictionary using its __dict__ attribute
            # This way, each object's attributes are stored as JSON key-value pairs
            json.dump([obj.__dict__ for obj in data], file, indent=4)

    @staticmethod
    def load_data(filename):
        """
        Load data from a JSON file and convert it into a list of objects.

        Args:
            filename (str): The file from which data will be loaded.

        Returns:
            list: A list of objects loaded from the JSON file.
        """
        # Open the file in read mode and load the JSON content
        with open(filename, 'r') as file:
            data = json.load(file)
            # Convert each JSON object (dict) back into the corresponding Python object
            return [Storage._dict_to_object(obj) for obj in data]

    @staticmethod
    def _dict_to_object(data):
        """
        Convert a dictionary back into its corresponding object.

        Args:
            data (dict): The dictionary representation of the object.

        Returns:
            object: A Book, User, or Checkout object created from the dictionary.

        Raises:
            ValueError: If the dictionary doesn't match any known object type.
        """
        # Determine the type of object based on its attributes and return the corresponding object
        if 'isbn' in data and not 'user_id' in data:
            # If the dictionary has an 'isbn' key but not 'user_id', it's a Book object
            return Book(**data)
        elif 'user_id' in data and not 'isbn' in data:
            # If the dictionary has a 'user_id' key but not 'isbn', it's a User object
            return User(**data)
        elif 'checkout_date' in data:
            # If the dictionary has a 'checkout_date' key, it's a Checkout object
            return Checkout(**data)
        
        # If none of the conditions match, we don't know what kind of object this is
        raise ValueError("Unknown object type")
