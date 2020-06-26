def main():

    print ("Do you have coronavirus or the common flu?")

    def corona():
        print("you have coronavirus")
        sys.end()
   
    color = input("What is your skin color? ")
    if (color == "yellow"):
        corona()
    else:
        print("continue")

    travel = input("Have you traveled to mainland china in the past 2 weeeks? ")
    if (travel == "yes"):
        corona()
    else:
        print("continue")
    
    contact = input("has anyone you've been in close contact with been to mainland china in the past 2 weeks? ")
    if (contact == "yes"):
        corona()
    else:
        print("continue")
        
    aches = input("Do you have any pains or aches? ")
    if (aches == "yes"):
        corona()
    else:
        print("continue")
        
    breath = input("Do you have a shortness of breath? ")
    if (breath == "yes"):
        corona()
    else:
        print("Congradulations, you are suffering from the common flu!")

  

    

main()
