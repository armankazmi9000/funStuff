def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


def main ():
    enter = False
    while not enter:
        try:
            n1 = float(input("Enter your number 1."))
            n2 = float(input("Enter your number 2."))
            operation = int(input("Enter 1.+, 2.-, 3.*, or 4./"))
            enter = True 
        except:
            print("Invalid!!!!")
        
    if (operation == 1):
        print ("adding...")
        print (add(n1, n2))
        
    elif (operation == 2):
        print ("subtracting...")
        print (sub(n1, n2))

    elif (operation == 3):
        print ("multiplying...")
        print (mult(n1, n2))

    elif (operation == 4):
        print ("dividing...")
        print (div(n1, n2))

    else:
        print("Me no understand u")

main()
        
