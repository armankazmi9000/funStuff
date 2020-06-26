def main():

    bigcircle = float(input("What is the radius of the biggest circle on the outside in feet? "))

    smallcircle = float(input("What is the radius of the smallest circle in feet? "))

    bigarea = (bigcircle * bigcircle * 3.14159)

    smallarea = (smallcircle * smallcircle * 3.14159)

    totalarea = (bigarea - smallarea)

    print("Your total area in square feet is.......")
    print(totalarea) 
main()

    
