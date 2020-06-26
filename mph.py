print("A GAME IF UR BORED!!!!")

print("Mile Time Calculator")

d = int(input("how many miles did you run?"))

def response():
    print("nice work")
def badresponse():
    print("GET SOME EXCERCISE!")
def sleeplittle():
    print("SLEEP MORE!!")
def sleepbig():
    print("WAKE UP!!")
    
if(d == 0):
    badresponse() 
else:
    response()

t = int(input("How many minutes did you run?"))

if(t == 0):
    badresponse()
else:
    response()

def divide(d, t):
    return t / d

def mph():
    print(divide(d, t))
print("Your mile time is.............")
mph()


print("SLEEP calculator")

x = int(input("how many hours did u sleep last night?"))

if(x<7):
    sleeplittle()
if(x>9):
    sleepbig()
if (x == 7):
    reponse()
if (x == 8):
    reponse()
if (x == 9):
    reponse()

if(x<7):
    sleeplittle()
if(x>9):
    sleepbig()
if (x == 7):
    reponse()
if (x == 8):
    reponse()
if (x == 9):
    reponse()

if(x<7):
    sleeplittle()
if(x>9):
    sleepbig()
if (x == 7):
    reponse()
if (x == 8):
    reponse()
if (x == 9):
    reponse()
    
print("sleep better tomorrow night:)")


print("Total Price Calculator")


pl = int(input("how many units did u buy?"))

def cheap():
    print("good deal!!")
def expensive():
    print("rip off!!")

pr = int(input("How many dollars was each unit?"))

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

    


