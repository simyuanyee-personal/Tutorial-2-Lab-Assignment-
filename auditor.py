#Set Inventory as 0
inventory = 0
failed = 0

while True:
    print ("===================")
    print ("Please enter 2 to view current inventory amount")
    print ("Please enter 1 to input your stock quantity")
    print ("Please enter 0 to exit the program")
    choice = (input("Enter your Choice here  "))
    if not choice.isdigit():
        print("Error: Please enter a valid number.")
        failed += 1

    choice = int(choice)

    if choice == 2:
        print (inventory)

    if choice == 1:
        stock = (input("Please enter the stock amount"))
        stock = int(stock)
        inventory = inventory + stock

    if choice == 0:
        print (inventory)
        break

    if inventory > 500:
        print ("Error, Current inventory amount exceeded 500")
        break
