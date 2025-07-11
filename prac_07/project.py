class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        """Represents a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __str__(self):
        """Returns a string representation of the project."""
        date_str = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}, start = {date_str}, priority = {self.priority}, cost = ${self.cost_estimate:.2f}, completion = {self.completion_percent}%)"

    def __lt__(self, other):
        """Compare projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Returns True if the project is complete."""
        return self.completion_percent == 100