#program to give information on user's polynomial equation
import math
import cmath

def main():
    print("Polynomial Solver")
    print("")
    while True:
        what = input("Would you like to solve a quadratic or a cubic? ")
        if (what.lower() == "quadratic"):
            #function to give information on user's quadratic equation
            print("")
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
                return()


            elif (discriminant == 0):
                print("")
                print("There are 2 equal solutions")
                print(f"x = {round(firstanswer,5)} and {round(firstanswer,5)}") 
                returnInfo()
                return()


        elif(what.lower() == "cubic"):
            #function to give information on user's cubic equation
            print("")
            print("Cubic Solver")
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
            #get the 4 coefficients from user for the equation
            a = inputNumber("What is the A value in the quadratic function? ")
            b = inputNumber("What is the B value in the quadratic function? ")
            c = inputNumber("What is the C value in the quadratic function? ")
            d = inputNumber("What is the D value in the quadratic function? ")

            #calculations to determine number of solutions
            f = ((3 * (c / a)) - ((b ** 2) / (a ** 2))) / 3
            g = (((2 * (b ** 3)) / (a ** 3)) - ((9 * b * c) / (a ** 2)) + ((27 * d) / a)) / 27
            h = (((g ** 2) / 4) + ((f ** 3) / 27))

            if (h > 0):

                R = (-1 * (g / 2) + (h)**(0.5))
                if R >= 0:
                    S = R**(1/3)
                elif R < 0:
                    S = -1 * (abs(R)**(1/3))
                    
                T = (((-1) * (g / 2)) - (h)**(0.5))
                if T >= 0:
                    U = T**(1/3)
                elif T < 0:
                    U = -1 * (abs(T)**(1/3))
    


                x1 = (S + U)-(b/(3*a))
                aa = -1*((S+U)/2)
                bb = (b/(3*a))
                cc = ((S-U)*math.sqrt(3))/2
                x2 = (aa-bb)
                x3 = (aa-bb)

                print("")
                print("There is 1 real solution and 2 imaginary solutions")
                print(f"x = {round(x1,5)}, {round(x2,5)} + {round(cc,5)}j, and {round(x3,5)} - {round(cc,5)}j")
                return()
             

            elif (h == 0 and f == 0 and g == 0):

                x = ((d / a)**(1/3)) * -1
                print("")
                print("There are 3 equal solutions")
                print(f"x = {round(x,5)}, {round(x,5)}, and {round(x,5)}")
                return()

            elif (h <= 0):

                i = (((g ** 2)/4) - h)**(0.5)
                j = (i)**(1/3)
                k = math.acos(-1 *(g / (2 * i)))
                L = (j * -1)
                M = math.cos(k / 3)
                N = ((math.sqrt(3)) * math.sin(k / 3))
                P = (b / (3 * a)) * -1
                
                x1 = ((2 * j) * M) + P
                x2 = (L * (M + N)) + P
                x3 = (L * (M - N)) + P

                print("")
                print ("There are 3 real solutions")
                print (f"x = {round(x1,5)}, {round(x2,5)}, and {round(x3,5)}")
                return()
            

        else:
            print("Sorry we do not understand. Please try again")
            continue



main()
