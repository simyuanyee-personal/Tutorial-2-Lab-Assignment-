import json
import os
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Shipping import Shipping

Inventory_file = "inventory.json"

# Maps the "type" identifier stored in the JSON file to the class that rebuilds it.
# To support a new product type, add its class here (each class sets PRODUCT_TYPE).
PRODUCT_TYPES = {cls.PRODUCT_TYPE: cls for cls in (PhysicalProduct, DigitalProduct)}


# ---------------------------------------------------------------
# File handling (JSON <-> Product objects)
# ---------------------------------------------------------------
def load_inventory():
    """Load inventory.json into an Inventory object, or return an empty one."""
    if not os.path.exists(Inventory_file):
        print(f"{Inventory_file} not found. Starting with an empty inventory.")
        return Inventory()

    print(f"{Inventory_file} found.")
    try:
        with open(Inventory_file, "r") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Unexpected file structure")

        inventory = Inventory()
        for item in data:
            # Records saved before Lab 7 have no "type"; they were all physical goods.
            product_class = PRODUCT_TYPES[item.get("type", "physical")]
            inventory.add_product(product_class.from_dict(item))
        print("Inventory loaded successfully.")
        return inventory
    except (json.JSONDecodeError, ValueError, KeyError, TypeError):
        print("Error: Inventory file is corrupted. Starting with an empty inventory.")
        return Inventory()


def save_inventory(inventory):
    """Convert each product to a dictionary (including its type) and write to inventory.json."""
    data = [product.to_dict() for product in inventory.get_products()]
    with open(Inventory_file, "w") as file:
        json.dump(data, file, indent=4)
    print("Inventory saved successfully!")


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


def create_product(product_id, name, price, stock):
    """Ask which type of product to add, collect its extra detail and build it.

    Returns a PhysicalProduct / DigitalProduct, or None if the input was invalid.
    """
    print("\nProduct Type")
    print("1. Physical Product")
    print("2. Digital Product")
    choice = input("Choose type: ").strip()

    if choice == "1":
        weight = get_number("Weight (kg): ", float)
        if weight is None:
            print("\nError: Weight must be a valid non-negative number.")
            return None
        return PhysicalProduct(product_id, name, price, stock, weight)

    if choice == "2":
        download_size = get_number("Download Size (MB): ", float)
        if download_size is None:
            print("\nError: Download size must be a valid non-negative number.")
            return None
        return DigitalProduct(product_id, name, price, stock, download_size)

    print("\nError: Please choose 1 or 2.")
    return None


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
            inventory.display_all()

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
            new_id = inventory.generate_product_id()
            product = create_product(new_id, name, price, stock)
            if product is None:
                continue
            inventory.add_product(product)
            print(f"\nProduct added successfully! Assigned ID: {new_id}")

        elif option == "3":
            print("\nDelete Product")
            product_name = input("Product Name: ").strip()
            if inventory.delete_product(product_name):
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
            if inventory.update_stock(product_name, amount):
                print("\nStock updated successfully!")
            else:
                print("\nError: Product not found, or stock would drop below zero.")

        elif option == "5":
            print("\nSearch Product")
            query = input("Enter Product Name: ")
            product = inventory.search_product(query)
            if product:
                print("\nProduct found:")
                product.display_information()
                print(f"    Fulfilment: {product.get_fulfilment_info()}")
                if isinstance(product, CanBeShipped):
                    print(f"    Shipping cost: ${product.calculate_shipping_cost():.2f}")
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
            print("\nError: Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()