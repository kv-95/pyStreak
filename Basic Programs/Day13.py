# Python Program for Sum of squares of first n natural numbers	

def sumofSquares(n):
    sum = 0
    for i in range(n+1):
        sum += i*i
    return sum
    

if __name__ == "__main__":
    n = int(input("Enter the value of n : "))
    print("Sum of squares of first {} natural numbers : {}".format(n,sumofSquares(n)))