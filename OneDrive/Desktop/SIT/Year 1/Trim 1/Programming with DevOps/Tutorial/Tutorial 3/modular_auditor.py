#Set Inventory as 0 and also set Failed as 0 to record all the failed attempts
inventory = 0
failed = 0

#Created the infinite loop for the main menu for user to interact with 
while True:
    print ("===================")
    print ("Please enter 2 to view current inventory amount")
    print ("Please enter 1 to input your stock quantity")
    print ("Please enter 0 to exit the program")
#input to allow users to input their choice
    choice = (input("Enter your Choice here  "))
#checks if choice is a int and that the number is not negative, if it is prints a error message and add to the failed attempt
    if not choice.isdigit() or int(choice) < 0:
        print("Error: Please enter a valid number.")
        failed += 1
        continue

#changes choice from a string to a int, makes it easier for the if statement below as can just equal to a number
    choice = int(choice)

#if choice is 2, it will show the current inventory amounnt
    if choice == 2:
        print (inventory)
#if choice is 1, asks users to input their stock amount they wanna
    elif choice == 1:
        stock = (input("Please enter the stock amount"))
        if not stock.isdigit() or int(choice) < 0:
            print ("Error: Please enter a valid number")
            failed += 1
            continue
        stock = int(stock)
        inventory = inventory + stock

#if choice is 0 or above 500, immediately breaks the loop and prints a error message
    elif choice == 0:
        print (inventory)
        print ("Number of failed entries  ",failed)
        break

    if inventory > 500:
        print ("Error: Current inventory amount exceeded 500")
        print ("Number of failed entries  ",failed)
        break
