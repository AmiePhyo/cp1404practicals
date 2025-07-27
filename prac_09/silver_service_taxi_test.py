"""
CP1404/CP5632 Practical
Test code for SilverServiceTaxi
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    # Create a fancy taxi (fanciness = 2)
    fancy_taxi = SilverServiceTaxi("Hummer", fuel=100, fanciness=2)

    fancy_taxi.start_fare()
    fancy_taxi.drive(18)

    expected_fare = 48.78
    actual_fare = fancy_taxi.get_fare()
    print(f"Fare for 18 km in SilverServiceTaxi: ${actual_fare}")
    assert actual_fare == expected_fare, f"Expected ${expected_fare}, but got ${actual_fare}"

    print(fancy_taxi)

test_silver_service_taxi()
