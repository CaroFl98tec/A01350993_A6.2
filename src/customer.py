from src.storage import Storage
import uuid

class Customer:
    def __init__(self, name, email):
        self.customer_id = str(uuid.uuid4())
        self.name = name
        self.email = email

    def update_name(self, new_name):
        self.name = new_name

    def update_email(self, new_email):
        self.email = new_email