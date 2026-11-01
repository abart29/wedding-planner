import dataclasses
from decimal import Decimal


@dataclasses.dataclass
class Venue:
    name: str
    location: str
    capacity: int
    deposit: Decimal
    price: Decimal

    def __post_init__(self) -> None:
        if self.capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        if self.deposit < 0:
            raise ValueError("Deposit must be a non-negative decimal.")
        if self.price < 0:
            raise ValueError("Price must be a non-negative decimal.")

    def __str__(self) -> str:
        return f"{self.name} located at {self.location} with a capacity of {self.capacity} with a deposit of {self.deposit} and total price of {self.price}"
