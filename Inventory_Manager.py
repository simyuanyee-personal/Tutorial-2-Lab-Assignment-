import json
import os

Inventory_file = "inventory.json"


# ---------------------------------------------------------------
# Data persistence
# ---------------------------------------------------------------
def load_inventory():
    """Load inventory.json if it exists, otherwise begin with an empty inventory."""
    if not os.path.exists(Inventory_file):
        print(f"{Inventory_file} not found. Starting with an empty inventory.")
        return []

    print(f"{Inventory_file} found.")
    try:
        with open(Inventory_file, "r") as file:
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
    with open(Inventory_file, "w") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully!")


# ---------------------------------------------------------------
# Data manipulation
# ---------------------------------------------------------------
def search_product(inventory, query):
    """Return the product whose ID or name matches query (case-insensitive), else None."""
    query = query.strip().lower()
    for product in inventory:
        if product["id"].lower() == query or product["name"].lower() == query:
            return product
    return None


def generate_product_id(inventory):
    """Return the next ID in the form P001, P002, ... based on the highest existing one."""
    numbers = [int(p["id"][1:]) for p in inventory if p["id"][1:].isdigit()]
    return f"P{max(numbers, default=0) + 1:03d}"


def add_product(inventory, name, price, stock):
    """Add a new product with an auto-generated ID. Returns the new product's ID."""
    product_id = generate_product_id(inventory)
    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock,
    }
    inventory.append(product)
    return product_id

def delete_product(inventory, product_name):
    """Delete a product by name. Returns True if deleted, False if not found."""
    product = search_product(inventory, product_name)
    if product is None:
        return False
    inventory.remove(product)
    return True


def update_stock(inventory, product_name, amount):
    """Apply a transaction (+ delivery, - sale) to a product found by name.
    Returns False if not found or stock would drop below zero."""
    product = search_product(inventory, product_name)
    if product is None or product["stock"] + amount < 0:
        return False

    product["stock"] += amount
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


# ---------------------------------------------------------------
# Input helpers and menu
# ---------------------------------------------------------------
def get_number(prompt, number_type, allow_negative=False):
    """Return a number of number_type (int or float), or None if invalid."""
    try:
        value = number_type(input(prompt).strip())
    except ValueError:
        return None
    if value < 0 and not allow_negative:
        return None
    return value


def show_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Delete Product")
    print("4. Update Stock")
    print("5. Search Product")
    print("6. Save Inventory")
    print("7. Exit")
    print("----------------------------")


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
            name = input("Product Name: ").strip()
            if not name:
                print("\nError: Product name cannot be empty.")
                continue
            price = get_number("Price: ", float)
            stock = get_number("Stock Quantity: ", int)
            if price is None or stock is None:
                print("\nError: Price and stock must be valid non-negative numbers.")
                continue
            new_id = add_product(inventory, name, price, stock)
            print(f"\nProduct added successfully! Assigned ID: {new_id}")

        elif option == "3":
            print("\nDelete Product")
            product_name = input("Product Name: ").strip()
            if delete_product(inventory, product_name):
                print("\nProduct deleted successfully!")
            else:
                print("\nError: Product not found.")


        elif option == "4":
            print("\nUpdate Stock")
            product_name = input("Product Name: ").strip()
            amount = get_number(
                "Stock Adjustment (positive for adding stock, negative for removing stock): ",
                int,
                allow_negative=True,
            )
            if amount is None:
                print("\nError: Please enter a valid whole number.")
                continue
            if update_stock(inventory, product_name, amount):
                print("\nStock updated successfully!")
            else:
                print("\nError: Product not found, or stock would drop below zero.")

        elif option == "5":
            print("\nSearch Product")
            query = input("Enter Product Name: ")
            product = search_product(inventory, query)
            if product:
                print("\nProduct found:")
                print(f"ID: {product['id']} | Name: {product['name']} | "
                      f"Price: ${product['price']:.2f} | Stock: {product['stock']}")
            else:
                print("\nProduct not found.")

        elif option == "6":
            save_inventory(inventory)

        elif option == "7":
            save_inventory(inventory)
            print("\nThank you for using the Inventory Management System.")
            print("Program Exited.")
            break

        else:
            print("\nError: Please enter a number from 1 to 6.")


main()