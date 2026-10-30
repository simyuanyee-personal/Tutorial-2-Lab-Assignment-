from Product import Product
from Shipping import Shipping


class PhysicalProduct(Product, Shipping):
    """A product that is stored in a warehouse and shipped to the customer.

    Inherits from Product (single class inheritance: a physical product
    IS-A product) and signs the Shipping interface (a physical product
    MUST-BE-ABLE-TO be shipped).
    """

    PRODUCT_TYPE = "physical"

    # Simple shipping rule: flat fee plus a charge per kilogram.
    BASE_SHIPPING_FEE = 5.00
    COST_PER_KG = 2.00

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        self.__weight = weight  # kilograms

    def get_weight(self):
        return self.__weight

    def display_information(self):
        """Common information from Product, plus this product's weight."""
        super().display_information()
        print(f"    Type: Physical | Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
        return "Physical product - requires storage and physical shipping."

    def calculate_shipping_cost(self):
        """Flat fee + a per-kilogram charge."""
        return self.BASE_SHIPPING_FEE + self.COST_PER_KG * self.__weight

    def to_dict(self):
        data = super().to_dict()
        data["weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, data):
        """Rebuild a PhysicalProduct from a saved dictionary."""
        return cls(data["id"], data["name"], data["price"], data["stock"],
                   data.get("weight", 0.0))