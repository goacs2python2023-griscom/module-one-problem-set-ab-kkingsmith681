"""Write a function that uses the previous function and returns the area of a circle. """

x = int(input("What is the radius of the circle? "))

def areaofcircle(x):
    return 3.1415 * x ** 2

print(areaofcircle(x))