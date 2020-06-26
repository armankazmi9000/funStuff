def main():
    print("Television Help")

    brand = (input("What brand television are you buying?.... Enter ALL LOWERCASE and SPELL CORRECTLY "))
    
    def good():
        print("Good Choice!")

    def bad():
        print("Bad Choice!")
    
    if(brand == "lg"):
            bad()

    if(brand == "samsung"):
            good()
            
    if(brand == "sony"):
            good()
            
    if(brand == "vizio"):
            good()


    cost = float(input("How much does the television cost in dollars? "))

    def goood():
        print("BUY ITTT")

    def middle():
        print("Okay thats fine")

    def baad():
        print("You can do better than that")

    def baadd():
        print("OUT OF MY BUDGET!")


    if(cost <= 1000):
            goood()

    if(1000 < cost < 2000):
            middle()

    if(2000 <= cost < 2500):
            baad()

    if(cost >= 2500):
            baadd()

    size = float(input("What is the size of the television in inches? "))

    def small():
        print("TOO SMALL")

    def big():
        print("Perfect")

    if(size < 80):
        small()

    if(size >= 80):
        big()

    finalchoice = input("Would you like to purchase this televison? yes or no, ALL LOWERCASE ")

    def yes():
        print("Okay, your total amount after tax is......")
        print(cost * 1.075)

    def no():
        print("YOU JUST WASTED MY TIME!")

    if(finalchoice == "no"):
        no()
    if(finalchoice == "yes"):
        yes()



    else:
        print("ME NO UNDERSTAND!")
        
       

main()
