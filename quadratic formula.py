def main():

    print("Quadratic Formula")

    a = float(input("What is the A value in the quadratic function? "))
    
    b = float(input("What is the B value in the quadratic function? "))

    c = float(input("What is the C value in the quadratic function? "))


    negativeb = (b * -1)
    
    bsquared = (b * b)

    fourac = (4 * a * c)

    discriminant = (bsquared - fourac)

    twoa = (2 * a)

    if (discriminant > 0):
        print("There are 2 solutions")


    if (discriminant == 0):
        print("There is 1 solution")


    elif (discriminant < 0):
        print("There are 2 imaginary solutions")


    import math

    sqaurerootdiscriminant = (math.sqrt(discriminant))

    positivetop = (negativeb + sqaurerootdiscriminant)

    negativetop = (negativeb - sqaurerootdiscriminant)

    firstanswer = (positivetop / twoa)

    secondanswer = (negativetop / twoa)

    print("x = ", end ="")
    print(firstanswer, end =" ")
    print("and ", end ="")
    print(secondanswer)

    

main()
