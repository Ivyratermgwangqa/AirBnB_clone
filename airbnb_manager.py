#!/usr/bin/env python3
"""
AirbnbObject and AirbnbUser classes for managing Airbnb entities.

Classes:
- AirbnbObject: Represents Airbnb object with a name and location.
- AirbnbUser: Represents an Airbnb user, inheriting from AirbnbObject.

Functions:
- display_info(): Displays information about Airbnb objects.
"""

class AirbnbObject:
    """Generic Airbnb object with name and location."""
    def __init__(self, name, location):
        self.name, self.location = name, location

    def display_info(self):
        """Display information about the Airbnb object."""
        print(f"Name: {self.name}, Location: {self.location}")


class AirbnbUser(AirbnbObject):
    """Airbnb user, inheriting from AirbnbObject."""
    def __init__(self, name, location, username, email):
        super().__init__(name, location)
        self.username, self.email = username, email

    def display_info(self):
        """Display information about the Airbnb user."""
        super().display_info()
        print(f"Username: {self.username}, Email: {self.email}")


def main():
    """Example usage of AirbnbUser class."""
    user = AirbnbUser("Daniel", "rwanda", "daniel_rwa", "daniel@123.com")
    user.display_info()


if __name__ == "__main__":
    main()
