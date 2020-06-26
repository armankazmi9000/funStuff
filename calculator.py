def main():
    print("Calculator")
    print("")

    arman = True
    
    while arman == True:
        def inputNumber(message):
            while True:
                try:
                    userInput = float(input(message))       
                except ValueError:
                    print("That's not a number! Try again.")
                    continue
                else:
                    return userInput 
                    break
        x = inputNumber("What is your first number: ") 
        op = input("What operation would you like to do(+,-,*,/): ")
        op = op.lower()

        while True:
            if op == "a" or op == "add" or op == "+" or op == "s" or op == "subtract" or op == "-" or op == "m" or op == "multiply" or op == "*" or op == "d" or op == "divide" or op == "/":
                break
            else:
                print("I don't understand, try again")
                op = input("What operation would you like to do: ")
                continue
                
        y = inputNumber("What is your second number: ")

        print("")

        if (op == "a" or op == "add" or op == "+"):
            print(f"Sum is {round(x+y,10)}")

        elif (op == "s" or op == "subtract" or op == "-"):
            print(f"Difference is {round(x-y,10)}")

        elif (op == "m" or op == "multiply" or op == "*"):
            print(f"Product is {round(x*y,10)}")

        elif ( (y == 0) and (op == "d" or op == "divide" or op == "/") ):
            print("To infinity and beyond")

        elif (op == "d" or op == "divide" or op == "/"):
            print(f"Quotient is {round(x/y,10)}")

        print("")
        next = input("Would you like to do another operation: ")

        next = next.lower()
        if (next == "yes" or next == "y" or next == "ok" or next == "okay" or next == "ya"):
            print("")
            print("Great! Lets go!")
            arman = True
        else:
            arman = False
            
    print("okay, don't forget to like comment hashtag subscribe and turn the bell notifications on")

main()
