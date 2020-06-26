print("Average Grade calculator")

classes = int(input("how many classes do u have?"))

def zero():
    print("why are you even on this!")
def twoplus():
    print("well atleast u have a reason to be here!")
    
if(classes < 2):
    zero()
if(classes == 2):
    twoplus()
if(classes > 2):
    twoplus()


class1 = int(input("what is your grade percentage for ur first class?"))

def zero():
    print("why are you even on this!")
def twoplus():
    print("well atleast u have a reason to be here!")
def sleeplittle():
    print("SLEEP MORE!!")
def sleepbig():
    print("WAKE UP!!")

    
if(class1 == 0):
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
