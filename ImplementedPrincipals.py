def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

count = 1
print("Welcome to the Python Calculator!\n")
while (True):
    choice = int(input("Enter a Positive Number to perform a calculation or 0 and below to Exit: "))
    if(choice == 1):
        print(f'\nSession: {count}')
        a = int(input("Please enter a number for A: "))
        b = int(input("Please enter a number for B: "))
        print("Enter 1 for addition \nEnter 2 for subtraction \nEnter 3 for multiplication \nEnter 4 for division ")
        calculation = input("Please enter a number for Calculation: ")
        if(calculation == "1"):
            print(add(a, b))
        elif(calculation == "2"):
            print(subtract(a, b))
        elif (calculation == "3"):
            print(multiply(a, b))
        elif(calculation == "4"):
            print(divide(a, b))
        else:
            print("That is not a valid choice\n")
    else:
        break

    count += 1


