# Python Program for Cube Sum of first n natural numbers

def sumofCube(n):
    sum = 0
    for i in range(n+1):
        sum += i**3
    return sum

if __name__ == "__main__":
    n = int(input("Enter the value of n : "))
    print("Sum of cube of first {} natural numbers : {}".format(n,sumofCube(n)))