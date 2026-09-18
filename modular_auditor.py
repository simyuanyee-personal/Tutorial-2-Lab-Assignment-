#Set Inventory as 0 and also set Failed as 0 to record all the failed attempts
inventory = 0
failed = 0

def get_valid_input():
    #Created the infinite loop for the main menu for user to interact with 
    while True:
        print("===================")
        print("Please enter 2 to view current inventory amount")
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
        if choice not in [0, 1, 2]:
            print("Error: Please enter 0, 1, or 2.")
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
    
#Created the infinite loop for the main menu for user to interact with 
    while True:
        choice = get_valid_input()
        if choice == 1:
            stock = input("Please enter the stock amount: ")
            process_delivery(inventory, int(stock))
            calculate_tax(new_total)
            if not stock.isdigit() or int(stock) < 0:
                print("Error: Please enter a valid number.")
                failed += 1
                continue
            continue

        elif choice == 0:
            generate_report(inventory, failed)
            print("Exiting the program. Goodbye!")
            break
