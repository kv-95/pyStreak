# Area of circle

import math

def area(r):
    PI = math.pi
    return PI*r**2

if __name__ == "__main__":

    r = float(input("Enter the radius of circle: "))
    a = area(r)

    print("Area of the circle of radius {:f} m is {:0.3f} sq.meter".format(r,a))