# tests/test_customer.py
import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Carolina", "c@example.com")

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "Carolina")
        self.assertEqual(self.customer.email, "c@example.com")

    def test_customer_update_name(self):
        self.customer.name = "Ana"
        self.assertEqual(self.customer.name, "Ana")

    def test_customer_update_email(self):
        self.customer.email = "ana@example.com"
        self.assertEqual(self.customer.email, "ana@example.com")