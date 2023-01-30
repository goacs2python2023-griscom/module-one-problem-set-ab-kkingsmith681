""" Write a function that is given the month, day, and year of each of two dates (six arguments in all!), and determines which date comes earlier.  Return the string "before" if the first date comes before the second one, "after" if the first date comes after the second one, and "same" if they are the same. """

def earlierdate(year1, month1, day1, year2, month2, day2):

    if year1 > year2:
        return "after"
    elif year1 < year2:
        return "before"
    elif year1 == year2 and month1 > month2:
        return "after"
    elif year1 == year2 and month1 < month2:
        return "before"
    elif year1 == year2 and month1 == month2 and day1 > day2:
        return "after"
    elif year1 == year2 and month1 == month2 and day1 < day2:
        return "before"
    else:
        return "same"

print(earlierdate(2009,11,4, 2009, 10, 3))