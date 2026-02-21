# tests/test_reservation.py
import unittest
from src.hotel import Hotel
from src.customer import Customer
from src.reservation import Reservation

class TestReservation(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel("Hilton", 1)
        self.customer = Customer("Carolina", "c@example.com")
        self.reservation = Reservation(self.customer, self.hotel)

    def test_make_reservation_success(self):
        self.assertTrue(self.reservation.make_reservation())
        self.assertEqual(self.hotel.rooms, 0)

    def test_make_reservation_fail(self):
        self.hotel.rooms = 0
        self.assertFalse(self.reservation.make_reservation())

    def test_cancel_reservation_success(self):
        self.reservation.make_reservation()
        self.assertTrue(self.reservation.cancel())
        self.assertEqual(self.hotel.rooms, 1)

    def test_cancel_reservation_fail(self):
        self.assertFalse(self.reservation.cancel())