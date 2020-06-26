def add(num1, num2):
    """Returns num1 plus num2."""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2."""
    return num1 - num2


def mul(num1, num2):
    """Returns num1 times num2."""
    return num1 * num2


def div(num1, num2):
    """Returns num1 divided by num2."""
    return num1 / num2


def main():
    """Allows user to run basic calculator operations with two numbers."""
    validInput = False
    while not validInput:
        # Get user input
        try:
            num1 = int(input("What is number 1?"))
            num2 = int(input("What is number 2?"))
            operation = int(input("What do you want to do? 1. add, 2. subtract, 3. multiply, or 4. divide. Enter  number: "))
            validInput = True
        except:
            print("Invalid input. Try again.")
    # Determine operation
    if (operation == 1):
        print("Adding...")
        print(add(num1, num2))
    elif (operation == 2):
        print("Subtracting...")
        print(sub(num1, num2))
    elif (operation == 3):
        print("Multiplying...")
        print(mul(num1, num2))
    elif (operation == 4):
        print("Dividing...")
        print(div(num1, num2))
    else:
        print("I don't understand")


main()




print("Average Grade Percent Calculator")

1, 2, 3, 4, 5, 6, 7 = int(input("Enter your grade percentages, seperate each percent by a comma"))


