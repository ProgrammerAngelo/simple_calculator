#add a method that allows the user to pick between the operation: addition,subtraction,multiplication,division

#add a method for "try" function for detecting the error

#add a method for addition
print("\nAddition")
def addition():
    number_1 = float(input("Enter first number:\n"))
    number_2 = float(input("Enter second number:\n"))
    sum = number_1 + number_2
    print("The sum is:\n",sum)
addition()

#add a method for subtraction
print("\nSubtraction")
def subtraction():
    number_1 = float(input("Enter first number:\n"))
    number_2 = float(input("Enter second number:\n"))
    difference = number_1 - number_2
    print("The difference is:\n",difference)
subtraction()

#add a method for multiplication
print("\nMultiplication")
def multiplication():
    number_1 =float(input("Enter first number:\n"))
    number_2 = float(input("Enter second number:\n"))
    product = number_1 * number_2
    print("The difference is:\n",product)
multiplication()

#add a method for division
print("\nDivision")
def division():
    while True:
        number_1 =float(input("Enter first number:\n"))
        number_2 = float(input("Enter second number:\n"))
        if number_2 == 0:
            print("You cannot devide a number by zero!")
            print("Please enter a number other that Zero(0)")
        else:
            qoutient = number_1 / number_2
            print("The difference is:\n",qoutient)
            break
division()
#add a font,and colors for the text
