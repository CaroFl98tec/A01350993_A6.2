from src.storage import StorageManager


class Customer:
    """Represents a customer in the reservation system."""

    FILE_PATH = "data/customers.json"

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert customer object to dictionary."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
        }

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """Create a new customer."""
        customers = StorageManager.read_file(cls.FILE_PATH)

        if any(c["customer_id"] == customer_id for c in customers):
            raise ValueError("Customer already exists")

        customer = cls(customer_id, name, email)
        customers.append(customer.to_dict())
        StorageManager.write_file(cls.FILE_PATH, customers)

    @classmethod
    def delete_customer(cls, customer_id):
        """Delete an existing customer."""
        customers = StorageManager.read_file(cls.FILE_PATH)
        updated_customers = [
            c for c in customers if c["customer_id"] != customer_id
        ]

        if len(customers) == len(updated_customers):
            raise ValueError("Customer not found")

        StorageManager.write_file(cls.FILE_PATH, updated_customers)

    @classmethod
    def display_customer(cls, customer_id):
        """Return customer information."""
        customers = StorageManager.read_file(cls.FILE_PATH)

        for customer in customers:
            if customer["customer_id"] == customer_id:
                return customer

        raise ValueError("Customer not found")

    @classmethod
    def modify_customer(cls, customer_id, name=None, email=None):
        """Modify customer information."""
        customers = StorageManager.read_file(cls.FILE_PATH)
        found = False

        for customer in customers:
            if customer["customer_id"] == customer_id:
                if name:
                    customer["name"] = name
                if email:
                    customer["email"] = email
                found = True

        if not found:
            raise ValueError("Customer not found")

        StorageManager.write_file(cls.FILE_PATH, customers)