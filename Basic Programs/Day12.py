# Python Program for n\’th multiple of a number in Fibonacci Series

def findMultiple(n,k):
    a = 0
    b = 1
    count = 1
    while(True):
        c = a+b
        if c % k==0:
            if count == n:
                return(c)
            count += 1
        a,b = b,c

if __name__ == "__main__":
    k = int(input("Enter the number which is in the Fibonacci Series: "))
    n = int(input("Enter the value of n : "))
    print("{}th/nd/rd multiple of {} in Fibonacci Series is {}".format(n,k,findMultiple(n,k)))
