"""Write a Python function that computes the cost of a road trip, given the distance traveled, the fuel efficiency of the car (in miles per gallon), and the cost of a gallon of gas."""

def costoftrip(kilometers, kmpergallon, costofgallonofgas):
    total = (kilometers / kmpergallon) * costofgallonofgas
    return str(round(total,2))

print(costoftrip(235,8.1,4))