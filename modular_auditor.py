
def get_valid_input():
    #Created the infinite loop for the main menu for user to interact with 
    while True:
        print("===================")
        print("Please enter 1 to input your stock quantity")
        print("Please enter 0 to exit the program")

        choice = input("Enter your choice here: ")

    # Data validation to ensure the user user enters a valid number 
        if not choice.isdigit():
            print("Error: Please enter a valid number.")
            return None

        choice = int(choice)

    # Check whether choice is one of the valid options
        if choice not in [0, 1]:
            print("Error: Please enter 0 or 1.")
            return None

        return choice

#Added a function to process the delivery and calculate the new total inventory
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

#Added a function to calculate the tax amount based on the total inventory
def calculate_tax(amount):
    tax_rate = 0.10  # 10% tax rate
    tax_amount = amount * tax_rate
    return tax_amount

#Added a function to generate a report of the total units and failed attempts
def generate_report(total_units, failed_attempts):
    print("===================")
    print("Inventory Report")
    print("===================")
    print(f"Total Units: {total_units}")
    print(f"Failed Attempts: {failed_attempts}")

#Added a main function to run the program and handle user input
def main():
    inventory = 0
    failed = 0

#Created the infinite loop for the main menu for user to interact with 
    while True:
        choice = get_valid_input()

#Added a conditional statement to check the user input and process the delivery or exit the program
        if choice == 1:
            stock = input("Please enter the stock amount: ")

            if not stock.isdigit() or int(stock) < 0:
                print("Error: Please enter a valid number.")
                failed += 1
                continue

#Added a the ability for user to input their stock amount and process the delivery and calculate the tax amount
            stock =int(stock)
            new_stock= process_delivery(inventory, stock)
            tax = calculate_tax(new_stock)
            inventory = new_stock  # Update the inventory with the new stock amount
            print(f"Current inventory amount: {inventory}")
            print(f"Tax amount: {tax}")
            continue
#If the user enters 0, the program will generate a report and exit the program
        elif choice == 0:
            generate_report(inventory, failed)
            print("Program Exited.")
            break
        
#Main function is called to run the program
main()
