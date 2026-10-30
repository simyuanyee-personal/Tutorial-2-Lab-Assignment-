from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface-style contract for anything that can be shipped.

    Responsibility (ISP/SRP): describe ONE capability only - being shipped.
    It holds no attributes and no shipping logic; any class that "signs"
    this contract must provide its own calculate_shipping_cost().
    """

    @abstractmethod
    def calculate_shipping_cost(self):
        """Return the cost (float) of shipping this item."""
        pass