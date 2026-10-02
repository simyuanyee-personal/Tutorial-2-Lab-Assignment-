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
    inventory_list = load_inventory()
    failed = 0

    while True:
        choice = get_valid_input()

        # View inventory
        if choice == 2:
            print("Current inventory:")

            if not inventory_list:
                print("Inventory is empty.")
            else:
                for inventory_id, item, stock in inventory_list:
                    print(f"  ID: {inventory_id} | {item}: {stock}")

            continue

        # Add transaction
        if choice == 1:
            item = input("Please enter the item name: ")
            quantity = input("Please enter the amount for the item: ")

            if not quantity.isdigit() or int(quantity) < 0:
                print("Error: Please enter a valid number.")
                failed += 1
                continue

            quantity = int(quantity)

            # Check whether item already exists
            item_found = False

            for i in range(len(inventory_list)):

                inventory_id, existing_item, current_stock = inventory_list[i]

                if existing_item.lower() == item.lower():

                    new_stock = process_delivery(
                        current_stock,
                        quantity
                    )

                    inventory_list[i] = (
                        inventory_id,
                        existing_item,
                        new_stock
                    )

                    item_found = True
                    break

            # If item doesn't exist, add it
            if not item_found:

                if inventory_list:
                    new_id = max(
                        inventory_id
                        for inventory_id, item, stock in inventory_list
                    ) + 1
                else:
                    new_id = 1

                new_stock = process_delivery(0, quantity)

                inventory_list.append(
                    (new_id, item, new_stock)
                )


            print(f"Current inventory: {inventory_list}")

            continue

        # Exit
        elif choice == 0:
            save_inventory(inventory_list)

            generate_report(failed)

            print("===================")
            print("Thank you for using the inventory management system.")
            print("Program Exited.")

            break


main()
