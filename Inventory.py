class Inventory:
    """Manages a collection of Product objects.

    Responsibility (SRP): store, add, find, remove and display products.
    It does not read user input or touch files.
    """

    def __init__(self):
        self.__products = []

    def generate_product_id(self):
        """Return the next ID in the form P001, P002, ... based on the highest existing one."""
        numbers = []
        for product in self.__products:
            digits = product.get_product_id()[1:]
            if digits.isdigit():
                numbers.append(int(digits))
        return f"P{max(numbers, default=0) + 1:03d}"

    def add_product(self, product):
        """Store a Product object in the inventory."""
        self.__products.append(product)

    def search_product(self, query):
        """Return the product whose ID or name matches query, else None."""
        for product in self.__products:
            if product.matches(query):
                return product
        return None

    def delete_product(self, product_name):
        """Delete a product by name/ID. Returns True if deleted, False if not found."""
        product = self.search_product(product_name)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    def update_stock(self, product_name, amount):
        """Apply a stock transaction to a product found by name/ID.

        Returns False if not found or stock would drop below zero.
        """
        product = self.search_product(product_name)
        if product is None:
            return False
        return product.update_stock(amount)

    def display_all(self):
        """Print every product."""
        print("\nCurrent Inventory")
        print("-" * 47)
        if not self.__products:
            print("Inventory is empty.")
        for product in self.__products:
            product.display_information()
        print("-" * 47)

    def get_products(self):
        """Return a copy of the product list (so callers can't change the original list)."""
        return list(self.__products)