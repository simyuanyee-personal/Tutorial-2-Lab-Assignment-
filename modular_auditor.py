
def get_valid_input():
    #Created the infinite loop for the main menu for user to interact with 
    while True:
        print("===================")
        print("Please enter 1 to input your stock quantity")
        print("Please enter 0 to exit the program")

        choice = input("Enter your choice here: ")

    # Data validation
        if not choice.isdigit():
            print("Error: Please enter a valid number.")
            failed += 1
            return None

        choice = int(choice)

    # Check whether choice is one of the valid options
        if choice not in [0, 1]:
            print("Error: Please enter 0 or 1.")
            failed += 1
            return None

        return choice

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax_rate = 0.10  # 10% tax rate
    tax_amount = amount * tax_rate
    return tax_amount

def generate_report(total_units, failed_attempts):
    print("===================")
    print("Inventory Report")
    print("===================")
    print(f"Total Units: {total_units}")
    print(f"Failed Attempts: {failed_attempts}")


def main():
    inventory = 0
    failed = 0

#Created the infinite loop for the main menu for user to interact with 
    while True:
        choice = get_valid_input()
        if choice is None:
            failed += 1
            print ("Error: Please enter a valid number.")
            continue


        if choice == 1:
            stock = input("Please enter the stock amount: ")

            if not stock.isdigit() or int(stock) < 0:
                print("Error: Please enter a valid number.")
                failed += 1
                continue

            stock =int(stock)
            new_stock= process_delivery(inventory, stock)
            tax = calculate_tax(new_stock)
            inventory = new_stock  # Update the inventory with the new stock amount
            print(f"Current inventory amount: {inventory}")
            print (f"Tax amount: {tax}")
            continue

        elif choice == 0:
            generate_report(inventory, failed)
            print("Exiting the program. Goodbye!")
            break

main()
