from prac_09.unreliable_car import UnreliableCar

def main():
    """Test UnreliableCar over multiple drives to check behavior."""

    reliability = 30
    car = UnreliableCar("TestCar", fuel=1000, reliability=reliability)

    attempts = 100
    success_count = 0

    for i in range(attempts):
        distance = car.drive(1)  # try to drive 1 km each time
        if distance > 0:
            success_count += 1

    print(f"Attempts: {attempts}")
    print(f"Successful drives: {success_count}")
    print(f"Expected roughly: {reliability}% = {reliability / 100 * attempts}")

main()
