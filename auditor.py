#Set Inventory as 0
inventory = 0

while True:
    print ("===================")
    print ("Please enter 2 to view current inventory amount")
    print ("Please enter 1 to input your stock quantity")
    print ("Please enter 0 to exit the program")
    choice = int(input("Enter your Choice here  "))
    if choice == 2:
        print (inventory)

    if choice == 1:
        stock = int(input("Please enter the stock amount"))
        inventory = inventory + stock

    if choice == 0:
        break
