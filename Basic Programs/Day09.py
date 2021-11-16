# Python Program for n-th Fibonacci number

def fibonacci(n):
    f = [0,1]

    if n <= 0:
        return "Enter a valid number"
    elif n == 1 or n == 2:
        return n-1
    else:
        for i in range(n-2):
            fn = f[0] + f[1]
            f[0] = f[1]
            f[1] = fn
        return fn
if __name__ == "__main__":
    n = int(input("Enter number: "))
    print("{}th Fibonacci number is".format(n), fibonacci(n))
