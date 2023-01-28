"""Write a function that takes two arguments, one is the bill and the other is the percentage tip you would like to leave. The function should return the total for the bill."""

def tipCalculator(bill, percentTip):
    total = bill * (percentTip / 100 + 1)
    return "Your total is: " + str(round(total, 2))


print(tipCalculator(153, 8))
