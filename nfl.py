import random

team = (input("What NFL team do you think will win the Super Bowl? "))

foo = ["New Orleans Saints", "Los Angeles Rams", "Kansas City Chiefs", "Pittsburgh Steelers", "New England Patriots", "Chicago Bears", "Los Angeles Chargers", "Houston Texans", "Minnesota Vikings", "Green bay Packers", "Dallas Cowboys", "Denver Broncos"]
print("I think that the ", end ="")
print(random.choice(foo), end ="")
print(" would win, not the ", end ="")
print(team)




