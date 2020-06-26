print("A GAME IF UR BORED!!!!")

print("family game")
dad = input("whats ur dad's name?")

if(dad == "none"):
    print("k")
else:
    print("nice name")

mom = input("whats ur mom's name?")

if(mom == "none"):
    print("k")
else:
    print("nice name")

brother = input("whats ur bro's name?")

if(brother == "none"):
    print("k")
else:
    print("nice name")

sister = input("whats ur sister's name?")

if(sister == "none"):
    print("k")
else:
    print("nice name")

answer = input("enter brother/sister/mom/or dad, and i will randomly guess their name")

if(answer == "brother"):
    print(brother)
if(answer == "sister"):
    print(sister)
if(answer == "mom"):
    print(mom)
if(answer == "dad"):
    print(dad)
else:
    print("now try again")
    
answer = input("enter brother/sister/mom/or dad, and i will randomly guess their name")

if(answer == "brother"):
    print(brother)
if(answer == "sister"):
    print(sister)
if(answer == "mom"):
    print(mom)
if(answer == "dad"):
    print(dad)
else:
    print("")

print("i know i am a genius")


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

def idk():
    print("good way to rest")

def response():
    print("nice work")
def badresponse():
    print("GET SOME EXCERCISE!")
def sleeplittle():
    print("SLEEP MORE!!")
def sleepbig():
    print("WAKE UP!!")


if(x<7):
    sleeplittle()
if(x>9):
    sleepbig()
if (x == 7):
    idk()
if (x == 8):
    idk()
if (x == 9):
    idk()

if(x<7):
    sleeplittle()
if(x>9):
    sleepbig()
if (x == 7):
    idk()
if (x == 8):
    idk()
if (x == 9):
    idk()

if(x<7):
    sleeplittle()
if(x>9):
    sleepbig()
if (x == 7):
    idk()
if (x == 8):
    idk()
if (x == 9):
    idk()
    
print("sleep better tomorrow night:)")


print("Total Price Calculator")


pl = int(input("how many units did u buy?"))

def cheap():
    print("good deal!!")
def expensive():
    print("rip off!!")

pr = float(input("How many dollars was each unit?"))

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



