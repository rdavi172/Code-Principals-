# Basic Calculator Made in Python


#Add function adds the first input to the second input and returns value
def add(firstInput,secondInput ):
    return firstInput + secondInput

#subtract function subtracts the second input from the first and returns value
def subtract(firstInput,secondInput):
    return firstInput - secondInput

#multiply function takes first input and multiplies it by the second and returns value
def multiply(firstInput, secondInput):
    return firstInput * secondInput

#divide function takes the first input and divides it by the second and returns value
def divide(firstInput, secondInput):
    return firstInput / secondInput

#Variable that counts which session the user is on
sessionCount = 1


print("Welcome to the Python Calculator!\n")

#loop that keeps user implementing over the calculator
#Choice takes user input to determine whether to keep executing the calculator
#
while (True):
    choice = int(input("Enter a Positive Number to perform a calculation or 0 and below to Exit: "))
    if(choice == 1):
        print(f'\nSession: {sessionCount}')
        firstInput = int(input("Please enter your first number: "))
        secondInput = int(input("Please enter your second number: "))

        print("Enter 1 for addition \nEnter 2 for subtraction \nEnter 3 for multiplication \nEnter 4 for division ")
        calculationChoice = input("Please enter a number for Calculation: ")

        #Choice value for Add function
        if(calculationChoice == "1"):
            print(add(firstInput, secondInput))
        #Choice value for Subtract function
        elif(calculationChoice == "2"):
            print(subtract(firstInput, secondInput))
        #Choice value for Multiply function
        elif (calculationChoice == "3"):
            print(multiply(firstInput, secondInput))
        #Choice value for Divide function
        elif(calculationChoice == "4"):
            print(divide(firstInput, secondInput))
        else:
            print("That is not a valid choice\n")
    else:
        break

    sessionCount += 1

