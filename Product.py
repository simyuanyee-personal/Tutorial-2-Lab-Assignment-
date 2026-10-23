class Product:
    """Represents a single product and manages its own state.

    Responsibility (SRP): store product information and control how that
    information is changed. It does not load/save files, show menus or ask
    the user for input.
    """

    def __init__(self, product_id, name, price, stock):
        if price < 0 or stock < 0:
            raise ValueError("Price and stock cannot be negative.")
        # Double underscore = intended to be private (name mangling).
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # -----------------------------------------------------------
    # Read-only access to the attributes
    # -----------------------------------------------------------
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # -----------------------------------------------------------
    # Behaviour
    # -----------------------------------------------------------
    def update_stock(self, quantity):
        """Apply a transaction (+ delivery, - sale) to this product's stock.

        Returns True if applied, or False if stock would drop below zero
        (in which case the stock is left unchanged).
        """
        if self.__stock + quantity < 0:
            return False
        self.__stock += quantity
        return True

    def matches(self, query):
        """Return True if query equals this product's ID or name (case-insensitive)."""
        query = query.strip().lower()
        return self.__product_id.lower() == query or self.__name.lower() == query

    def display_information(self):
        """Print this product on one line."""
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")