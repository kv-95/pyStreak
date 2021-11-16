# Python Program for How to check if a given number is Fibonacci number

def fibList(num):
    if num == 0:
        return [0]
    a = 0
    b = 1
    c = a+b
    fib = [a, b]
    while c <= num:
        fib.append(c)
        a,b = b,c
        c = a+b
    return fib

def isFib(num):
    if num < 0 :
        print("Enter a valid number")
    elif fibList(num)[-1] == num:
        print("Given number, {} is a Fibonacci Number.".format(num))
    else:
        print("Given number, {} is NOT a Fibonacci Number.".format(num))

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    isFib(n)
    
