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
