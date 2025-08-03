class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician list."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return string representation of the Band and its members."""
        members_str = ", ".join(str(musician) for musician in self.members)
        return f"{self.name} ({members_str})"

    def __repr__(self):
        """Return representation of Band showing its internal dictionary."""
        return str(vars(self))

    def add(self, musician):
        """Add a Musician to the band."""
        self.members.append(musician)

    def play(self):
        """Return a string showing each member playing their first instrument (if any)."""
        return "\n".join(member.play() for member in self.members)
