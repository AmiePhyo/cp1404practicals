"""
ProgrammingLanguage class for CP1404/CP5632 Practical.

Estimate: 15 minutes
Actual: 7 minutes
"""


class ProgrammingLanguage:

    def __init__(self, programming_name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.programming_name = programming_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of the language."""
        return f"{self.programming_name}, {self.typing}, {self.reflection}, {self.year}"

    def is_dynamic(self):
        """Return True if typing is 'Dynamic', else False."""
        return self.typing == "Dynamic"