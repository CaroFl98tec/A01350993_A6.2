import unittest
from src.hotel import Hotel
from src.customer import Customer

class TestHotel(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel("Hilton", 2)
        self.customer = Customer("Carolina", "c@example.com")

    def test_reserve_room_success(self):
        self.assertTrue(self.hotel.reserve_room(self.customer))
        self.assertEqual(self.hotel.rooms, 1)

    def test_reserve_room_fail(self):
        self.hotel.rooms = 0
        self.assertFalse(self.hotel.reserve_room(self.customer))

    def test_cancel_reservation_success(self):
        self.hotel.reserve_room(self.customer)
        self.assertTrue(self.hotel.cancel_reservation(self.customer))
        self.assertEqual(self.hotel.rooms, 2)

    def test_cancel_reservation_fail(self):
        self.assertFalse(self.hotel.cancel_reservation(self.customer))