def main():

    height = float(input("Enter your height in inches. "))
    
    weight = float(input("Enter your weight in pounds. "))


    heightsquared = (height * height)
    
    jeff = (weight / heightsquared)

    bmi = (jeff * 703.0704)


    print("Your bmi is....")
    print (bmi)
    
    if (bmi <= 18.5):
        print ("You are underweight.")

    if (18.5 < bmi < 25):
        print ("You are normal weight.")

    if (25 <= bmi < 30):
        print ("You are overweight.")
        
    if (30 <= bmi < 40):
        print ("You are obese.")
        
    if (bmi >= 40):
        print ("You are extremely obese.")

main()



