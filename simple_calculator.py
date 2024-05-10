
# Add a method for addition
def addition():
    print("\nAddition")
    # Add a method for "try" function for detecting the error
    try:
        number_1 = float(input("Enter first number:\n"))
        number_2 = float(input("Enter second number:\n"))
        sum = number_1 + number_2
        print("The sum is:\n", sum)
    except:
        print("Invalid input! Please enter numbers only\n") 

# Add a method for subtraction
def subtraction():
    try:
        print("\nSubtraction")
        number_1 = float(input("Enter first number:\n"))
        number_2 = float(input("Enter second number:\n"))
        difference = number_1 - number_2
        print("The difference is:\n", difference)
    except:
        print("Invalid input! Please enter numbers only\n")

# Add a method for multiplication
def multiplication():
    print("\nMultiplication")
    try:
        number_1 =float(input("Enter first number:\n"))
        number_2 = float(input("Enter second number:\n"))
        product = number_1 * number_2
        print("The product is:\n", product)
    except:
        print("Invalid input! Please enter numbers only\n")

# Add a method for division
def division():
    print("\nDivision")
    while True:
        try:
            number_1 =float(input("Enter first number:\n"))
            number_2 = float(input("Enter second number:\n"))
            if number_2 == 0:
                print("You cannot divide a number by zero!")
                print("Please enter a number other than zero(0)")
            else:
                quotient = number_1 / number_2
                print("The difference is:\n", quotient)
                break
        except:
            print("Invalid input! Please enter numbers only\n")

# Add a method that allows the user to pick between the operation: addition, subtraction, multiplication, division
while True:
    print("\nHello User")
    print("Choose an operation\nEnter (1,2,3,4):")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choices = input("Enter your choice:\n")
    print("Your choice is: ",choices)

    if choices == "1":
        addition()
    elif choices == "2":
        subtraction()
    elif choices == "3":
        multiplication()
    elif choices == "4":
        division()
    else:
        print("Invalid input\nPlease choose a number between 1,2,3,4")
    
    try_again = input("Would you like to continue? (yes/no):\n")
    if try_again.lower() != "yes":
        print("Thank You!")
        break
# Add a font,and colors for the text
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
reset = '\033[0m'