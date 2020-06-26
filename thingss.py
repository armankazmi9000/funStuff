import random
foo = ["poop","pee","hike","eat","breathe"]

thing = (input("Would you like to do something today? "))

if thing == "yes":
    print("OK!, you should ", end ="")
    print(random.choice(foo))

else:
    print("Have fun bored") 


