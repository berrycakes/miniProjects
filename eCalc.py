# https://github.com/berrycakes/miniProjects/blob/master/eCalc.py

# Create a Python project to get the value of e to n number of decimal places.
print("""This prints the value of e to n number of decimal places""")

from math import e

def eDecimals(x):  #create a function called eDecimals
    if x > 15 and x < 0:
        print ("Please choose a number from 0-15")
    return round(e,x)

try: 
    decimal = int(input("How many decimal places? n = "))
    print(eDecimals(decimal))
except: #catch the error in case of non-integer input
    print("Please enter an integer")

 
