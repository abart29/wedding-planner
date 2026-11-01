import unittest
from decimal import Decimal

from wedding_planner.venues.venues import Venue


class TestVenue(unittest.TestCase):
    def setUp(self) -> None:
        self.venue = Venue(
            name="Grand Ballroom",
            location="Downtown",
            capacity=200,
            deposit=Decimal("1000.00"),
            price=Decimal("5000.00"),
        )

    def test_venue_creation(self) -> None:
        self.assertEqual(self.venue.name, "Grand Ballroom")
        self.assertEqual(self.venue.location, "Downtown")
        self.assertEqual(self.venue.capacity, 200)
        self.assertEqual(self.venue.deposit, Decimal("1000.00"))
        self.assertEqual(self.venue.price, Decimal("5000.00"))

    def test_venue_str(self) -> None:
        expected_str = "Grand Ballroom located at Downtown with a capacity of 200 with a deposit of 1000.00 and total price of 5000.00"
        self.assertEqual(str(self.venue), expected_str)

    def test_invalid_capacity(self) -> None:
        with self.assertRaises(ValueError):
            Venue(
                name="Small Hall",
                location="Uptown",
                capacity=0,
                deposit=Decimal("500.00"),
                price=Decimal("2000.00"),
            )
