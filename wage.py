def main():

    print("Take Home Salary Calculator")
    
    hourwage = float(input("How much money do you make per hour, in dollars($)?"))
    hoursperday = float(input("How many hours do you work per day?"))
    daysperweek = float(input("How many days do you work per week?"))
    daysoff = float(input("How many days do you take off per year, not including weekends?"))
    federaltax = float(input("How much federal tax to you pay, in percent(%)?"))
    statetax = float(input("How much state tax to you pay, in percent(%)?"))

    wageperday = (hourwage * hoursperday)
    daysperyear = (daysperweek * 52)
    daysperyeartotal = (daysperyear - daysoff)
    wage = (wageperday * daysperyear)
    federal = (federaltax / 100)
    federaltotal = (wage * federal)
    wagefederal = (wage - federaltotal)
    state = (statetax / 100)
    statetotal = (wage * state)
    totalwage = (wagefederal - statetotal)
    totaltotal = (totalwage / 26)
    
    print ("Your total take home salary is.....")
    print (totalwage)
    print ("Your total take home salary for 2 weeks is.....")
    print (totaltotal)

    if (totalwage > 50000):
        print("Your rich!!!!!")

    elif (totalwage < 50000):
        print("Better luck next time :(")
main()
