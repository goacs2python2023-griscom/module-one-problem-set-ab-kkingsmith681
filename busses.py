"""Write a function that determines the number of 52-passenger school buses needed to transport a given number of students."""
import math

def busses(students):
    x = students / 52
    x = math.ceil(x)
    return x

print(busses(1234))