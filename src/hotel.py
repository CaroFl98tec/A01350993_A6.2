# src/hotel.py

class Hotel:
    def __init__(self, name, total_rooms):
        self.name = name
        self.total_rooms = total_rooms
        # Cantidad de habitaciones libres (int)
        self.rooms = total_rooms
        # Reservas
        self.reservations = []

    def reserve_room(self, customer):
        if self.rooms <= 0:
            return False
        # Guardar reserva en dict
        reservation = {
            "hotel_name": self.name,
            "room": self.total_rooms - self.rooms + 1,
            "customer_name": customer.name
        }
        self.reservations.append(reservation)
        # Reducir habitaciones libres
        self.rooms -= 1
        return True

    def cancel_reservation(self, customer):
        for r in self.reservations:
            if r["hotel_name"] == self.name and r["customer_name"] == customer.name:
                self.reservations.remove(r)
                self.rooms += 1
                return True
        return False