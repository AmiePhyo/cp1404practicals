"""
Guitar class for CP1404/CP5632 Practical

Estimate: 15 minutes
Actual: 10 minutes
"""

class Guitar:
    """Represents a guitar"""
    def __init__(self, name="", year=0, cost=0):
        """Initialize a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return the age of the guitar"""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age(current_year) >= 50