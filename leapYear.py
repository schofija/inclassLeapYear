# isLeapYear takes 1 parameter (year) and tells the user whether or not it is a leap year
# returns 0 if NOT leap year
# returns 1 if leap year
# returns 2 if input is invalid (ie. user inputs "asdf" or some other non-integer)
def isLeapYear(year):
    try:
        int(year)
    except:
        print("Invalid input")
        return 2

    fourRem = int(year) % 4
    oneHundredRem = int(year) % 100
    fourHundredRem = int(year) % 400

    if fourRem != 0:
        print("Not a leap year")
        return 0
        
    else:
        if oneHundredRem == 0:
            if fourHundredRem != 0:
                print("Not a leap year")
                return 0
            else:
                print("Leap year!")
                return 1
        else:
            print("Leap year!")
            return 1