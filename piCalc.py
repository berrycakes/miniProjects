#Create a Python project to get the value of Pi to n number of decimal places.
print("""This prints the value of pi to n number of decimal places""")

from math import pi

def piDecimals(x):  #create a function called piDecimals
    if x > 15 and x < 0:
        return "Please choose a number from 0-15"
    return round(pi,x)

try: 
    decimal = int(input("How many decimal places? n = "))
    print(piDecimals(decimal))
except: #catch the error in case of non-integer input
    print("Please enter an integer")