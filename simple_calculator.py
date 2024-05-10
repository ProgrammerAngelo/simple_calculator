# Add a font,and colors for the text
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
magenta = '\033[35m'
cyan = '\033[36m'
light_gray = '\033[37m'
dark_gray = '\033[90m'
bright_red = '\033[91m'
bright_green = '\033[92m'
bright_yellow = '\033[93m'
bright_blue = '\033[94m'
bright_magenta = '\033[95m'
bright_cyan = '\033[96m'
white = '\033[97m'
Bbackground_black = '\033[40m'
background_red = '\033[41m'
background_green = '\033[42m'
Bbackground_yellow = '\033[43m'
background_blue= '\033[44m'
background_magenta = '\033[45m'
background_cyan = '\033[46m'
background_light_gray = '\third-party033[47m'
background_dark_gray = '\033[100m'
background_bright_red = '\033[101m'
background_bright_green = '\033[102m'
background_bright_yellow = '\033[103m'
background_bright_blue = '\033[104m'
background_bright_magenta = '\033[105m'
background_bright_cyan = '\033[106m'
background_white = '\033[107m'
reset = '\033[0m'

from pyfiglet import Figlet
font = Figlet(font = "doh", width = 200)
operation_font = Figlet(font = "big", width = 200)

# Add a method for addition
def addition():
    print("\n" + magenta +"Addition" + reset)
    # Add a method for "try" function for detecting the error
    try:
        number_1 = float(input("Enter first number:\n"))
        number_2 = float(input("Enter second number:\n"))
        sum = number_1 + number_2
        print( yellow + "The sum is:\n"+ reset, sum)
    except ValueError:
        print(red + "Invalid input! Please enter numbers only\n" + reset) 

# Add a method for subtraction
def subtraction():
    try:
        print("\n"+ cyan + "Subtraction" + reset)
        number_1 = float(input("Enter first number:\n"))
        number_2 = float(input("Enter second number:\n"))
        difference = number_1 - number_2
        print(yellow + "The difference is:" + reset + "\n" , difference)
    except:
        print("Invalid input! Please enter numbers only\n")

# Add a method for multiplication
def multiplication():
    print("\n" + bright_blue + "Multiplication" + reset)
    try:
        number_1 =float(input("Enter first number:\n"))
        number_2 = float(input("Enter second number:\n"))
        product = number_1 * number_2
        print(yellow + "The product is:" + reset + "\n", product)
    except:
        print("Invalid input! Please enter numbers only\n")

# Add a method for division
def division():
    print("\n" + black + "Division" + reset)
    while True:
        try:
            number_1 =float(input("Enter first number:\n"))
            number_2 = float(input("Enter second number:\n"))
            if number_2 == 0:
                print(red + "You cannot divide a number by zero!" + reset)
                print(green +"Please enter a number other than zero(0)" + reset)
            else:
                quotient = number_1 / number_2
                print(yellow + "The difference is:" + reset + "\n", quotient)
                break
        except:
            print(red + "Invalid input! Please enter numbers only" + reset + "\n")

# Add a method that allows the user to pick between the operation: addition, subtraction, multiplication, division
while True:
    print(bright_yellow + font.renderText("Hello User") + reset)
    print(green + operation_font.renderText("Choose an operation\n")+ reset + yellow + operation_font.renderText("Enter ( 1 , 2 , 3 , 4 ) :") + reset)
    print("1." + magenta + "Addition" + reset)
    print("2." + cyan + "Subtraction" + reset)
    print("3." + bright_blue + "Multiplication" + reset)
    print("4." + black + "Division" + reset)
    choices = input(background_bright_cyan + black + "Enter your choice:" + reset + "\n")
    print(green + "Your choice is: ", choices)

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
    
    try_again = input(yellow + "Would you like to continue?" + green + "(yes" + reset + "/"+ red + "no)" + ":\n" + reset)
    if try_again.lower() != "yes":
        print("Thank You!")
        break
