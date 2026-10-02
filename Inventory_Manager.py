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



def get_valid_input():
    while True:
        print("===================")
        print("Please enter 2 to view current inventory amount")
        print("Please enter 1 to input your transaction")
        print("Please enter 0 to exit the program")

        choice = input("Enter your choice here: ")

        # Data validation
        if not choice.isdigit():
            print("Error: Please enter a valid number.")
            continue

        choice = int(choice)

        # Check valid options
        if choice not in [0, 1, 2]:
            print("Error: Please enter 0, 1, or 2.")
            continue

        return choice


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def generate_report(failed_attempts):
    print("===================")
    print("Inventory Report")
    print("===================")
    print(f"Failed Attempts: {failed_attempts}")


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
