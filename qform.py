#program to give information on user's quadratic equation
import math
import cmath

def main():
    print("Quadratic Solver")
    print("")


    #function to make sure user enters a number
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
            
    #get the 3 coefficients from user for the equation
    a = inputNumber("What is the A value in the quadratic function? ")
    b = inputNumber("What is the B value in the quadratic function? ")
    c = inputNumber("What is the C value in the quadratic function? ")

    #calculates a variable to determine number of solution
    discriminant = ((b ** 2) - (4 * a * c))

    #calculates vertex
    x = (-1 * b)/(2 * a)
    y = (a * (x ** 2)) + (b * x) + (c)

    #function to return rest of info
    def returnInfo():
        print(f"y-int : (0, {round(c,5)})")
        print(f"vertex : ({round(x,5)}, {round(y,)})")
        print(f"Axis of Symmetry : x = {round(x,5)}")
        

    if (discriminant < 0):
        print("There are 2 imaginary solutions")
        root1 = (-b + cmath.sqrt(b**2 - 4 * a * c))/(2 * a)
        root2 = (-b - cmath.sqrt(b**2 - 4 * a * c))/(2 * a)
        print(f"x = {round(root1.real, 5) + round(root1.imag, 5) * 1j} and {round(root2.real, 5) + round(root2.imag, 5) * 1j}")
        returnInfo()
        return()

    
    #rest of calculations to determine solutions
    sqrtdiscriminant = (math.sqrt(discriminant))
    firstanswer = (((b * -1) + sqrtdiscriminant) / (2 * a))
    secondanswer = (((b * -1) - sqrtdiscriminant) / (2 * a))

    
    

    #prints info depending on number of solutions
    if (discriminant > 0):
        print("")
        print("There are 2 real solutions")
        print(f"x = {round(firstanswer,5)} and {round(secondanswer,5)}")
        returnInfo()


    elif (discriminant == 0):
        print("")
        print("There are 2 equal solutions")
        print(f"x = {round(firstanswer,5)} and {round(firstanswer,5)}") 
        returnInfo()


main()
