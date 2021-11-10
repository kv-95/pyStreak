# Python program to check whether a number is Prime or not

def isPrime(num):
    for i in range(2, int(num/2)+1):
        if num%i == 0:
            print("{} is a NOT a Prime Number!".format(num))
            return
    print("{} is a Prime Number!".format(num))

if __name__== '__main__':
    num =int(input("Enter the number (which should be greater than 1) : "))
    isPrime(num)
    
     