class User:
    def __init__(self, name, user_id, password):
        self.name = name
        self.user_id = user_id
        self.password = password

    def __str__(self):
        return f"User(name={self.name}, user_id={self.user_id})"
