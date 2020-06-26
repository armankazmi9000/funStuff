print("Total Price Calculator")


pl = int(input("how many things did u buy?"))

def cheap():
    print("good deal!!")
def expensive():
    print("rip off!!")

pr = float(input("How many dollars was each thing?"))

if(pr<5):
    cheap()
if(pr>5):
    response()
elif(pr==5):
    cheap()
    
def calc(pl,pr):
    return (((pr*pl)*0.075)+pr*pl)

def total():
    print(calc(pr,pl))
print("Your total price in $ is..")

total()
