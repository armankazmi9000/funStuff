def main():

    def cases():
        case = float(input("days: "))
        casesperday = (2.04507 *(1.27202 ** (case + 20)))
        print(casesperday)
        
    def days():
        day = float(input("cases: "))
        dayspercase = (log(day / 23.1087)/log(1.39919))
        print(dayspercase)

    question = input("Would you like to know the number of deaths in a certain amount of days or the number of days until a certain amount of deaths?(enter [cases] or [days] ")

    if (question == "cases"):
        cases()

    if (question == "days"):
        days()





main()

