# src/reservation.py

class Reservation:
    def __init__(self, customer, hotel):
        self.customer = customer
        self.hotel = hotel

    def make_reservation(self):
        return self.hotel.reserve_room(self.customer)

    def cancel(self):
        return self.hotel.cancel_reservation(self.customer)