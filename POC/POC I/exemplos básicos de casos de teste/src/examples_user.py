class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")
        if len(name) < 4:
            raise ValueError("Name must be at least 3 characters long")

    def update_password(self, new_password):
        self.password = new_password
        if len(new_password) < 6:
            raise ValueError("Password must be at least 6 characters long")

    def delete_account(self):
        del self
        if hasattr(self, 'name'):
            raise ValueError("Account was not deleted")