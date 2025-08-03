import random
from prac_09.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on its reliability."""

        driving_chance = random.randint(0, 100)
        if driving_chance < self.reliability:
            return super().drive(distance)
        else:
            print(f"{self.name} refused to drive! (Chance was {driving_chance})")
            return 0
