import json
import os

Inventory_File = "inventory.json"


def load_inventory():
    """Load inventory.json if it exists, otherwise begin with an empty inventory."""
    if not os.path.exists(Inventory_File):
        print(f"{Inventory_File} not found. Starting with an empty inventory.")
        return []

    print(f"{Inventory_File} found.")
    try:
        with open(Inventory_File, "r") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Unexpected file structure")
        print("Inventory loaded successfully.")
        return data
    except (json.JSONDecodeError, ValueError):
        print("Error: Inventory file is corrupted. Starting with an empty inventory.")
        return []


def save_inventory(inventory):
    """Write the inventory list to inventory.json."""
    with open(Inventory_File, "w") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully!")


def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

def search_product(inventory, query):
    """Return the product whose ID or name matches query (case-insensitive), else None."""
    query = query.strip().lower()
    for product in inventory:
        if product["id"].lower() == query or product["name"].lower() == query:
            return product
    return None

def add_product(inventory, product_id, name, price, stock):
    """Add a new product. Returns False if the ID is already in use."""
    if search_product(inventory, product_id) is not None:
        return False

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock,
        "history": [stock],  # every transaction amount is recorded here
    }
    inventory.append(product)
    return True

def update_stock(inventory, product_id, amount):
    """Apply a transaction (+ delivery, - sale) to a product found by ID.
    Returns False if not found or stock would drop below zero."""
    product = search_product(inventory, product_id)
    if product is None or product["stock"] + amount < 0:
        return False

    product["stock"] += amount
    product["history"].append(amount)
    return True

def display_all(inventory):
    """Print every product."""
    print("\nCurrent Inventory")
    print("-" * 47)
    if not inventory:
        print("Inventory is empty.")
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | "
              f"Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-" * 47)

def get_number(prompt, number_type, allow_negative=False):
    """Return a number of number_type (int or float), or None if invalid."""
    try:
        value = number_type(input(prompt).strip())
    except ValueError:
        return None
    if value < 0 and not allow_negative:
        return None
    return value


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    print()

    inventory = load_inventory()

    while True:
        show_menu()
        option = input("\nEnter option: ").strip()

        if option == "1":
            display_all(inventory)

        elif option == "2":
            print("\nAdd New Product")
            product_id = input("Product ID: ").strip()
            name = input("Product Name: ").strip()
            if not product_id or not name:
                print("\nError: Product ID and name cannot be empty.")
                continue
            price = get_number("Price: ", float)
            stock = get_number("Stock Quantity: ", int)
            if price is None or stock is None:
                print("\nError: Price and stock must be valid non-negative numbers.")
                continue
            if add_product(inventory, product_id, name, price, stock):
                print("\nProduct added successfully!")
            else:
                print(f"\nError: Product ID '{product_id}' already exists.")

        elif option == "3":
            print("\nUpdate Stock")
            product_id = input("Product ID: ").strip()
            amount = get_number(
                "Amount (positive = delivery, negative = sale): ",
                int,
                allow_negative=True,
            )
            if amount is None:
                print("\nError: Please enter a valid whole number.")
                continue
            if update_stock(inventory, product_id, amount):
                print("\nStock updated successfully!")
            else:
                print("\nError: Product not found, or stock would drop below zero.")

        elif option == "4":
            print("\nSearch Product")
            query = input("Enter Product ID or Name: ")
            product = search_product(inventory, query)
            if product:
                print("\nProduct found:")
                print(f"ID: {product['id']} | Name: {product['name']} | "
                      f"Price: ${product['price']:.2f} | Stock: {product['stock']}")
                print(f"Transaction history: {product['history']}")
            else:
                print("\nProduct not found.")

        elif option == "5":
            save_inventory(inventory)

        elif option == "6":
            save_inventory(inventory)
            print("\nThank you for using the Inventory Management System.")
            print("Program Exited.")
            break

        else:
            print("\nError: Please enter a number from 1 to 6.")


main()
