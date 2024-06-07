import random
import string

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, parking_lot, spot_number):
        if parking_lot.spots[spot_number] is None:
            parking_lot.spots[spot_number] = self
            return True, f"Car with license plate {self.license_plate} parked successfully in spot {spot_number}"
        else:
            return False, f"Car with license plate {self.license_plate} could not park in spot {spot_number}, spot already occupied."


class ParkingLot:
    def __init__(self, size, spot_width=8, spot_length=12):
        self.size = size
        self.spot_area = spot_width * spot_length
        self.num_spots = size // self.spot_area
        self.spots = [None] * self.num_spots

    def is_full(self):
        return all(spot is not None for spot in self.spots)


def generate_license_plate():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))


def main():
    # Define the size of the parking lot in square footage
    parking_lot_size = 2000  # Example size
    parking_lot = ParkingLot(parking_lot_size)

    # Generate a list of cars with random license plates
    num_cars = 25  # Example number of cars
    cars = [Car(generate_license_plate()) for _ in range(num_cars)]

    # Attempt to park each car in the parking lot
    for car in cars:
        while True:
            if parking_lot.is_full():
                print("Parking lot is full.")
                return
            spot_number = random.randint(0, parking_lot.num_spots - 1)
            success, message = car.park(parking_lot, spot_number)
            print(message)
            if success:
                break


if __name__ == "__main__":
    main()
