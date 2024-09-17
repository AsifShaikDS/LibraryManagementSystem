class User:
    def __init__(self, name, user_id, password):
        """
        Initialize a new User object.

        Args:
            name (str): The name of the user.
            user_id (str): The unique identifier for the user.
            password (str): The user's password (consider using hashed passwords in real applications).
        """
        self.name = name
        self.user_id = user_id
        self.password = password

    def __str__(self):
        """
        Provide a string representation of the User object.

        Returns:
            str: A string describing the User's name and user ID. 
                  Note: Password is not included in the string representation for security reasons.
        """
        return f"User(name={self.name}, user_id={self.user_id})"
