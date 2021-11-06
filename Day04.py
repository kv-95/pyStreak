# Python Program for compound interest

def compoundInterest(p,r,n,t):
    return p*((1 + r/n))**(n*t)
if __name__ == "__main__":
    p = float(input("Enter the Principal Amount (₹): "))
    r = float(input("Enter the Rate of Interest Rate : "))
    r=r/100
    t = float(input("Enter the number of time periods elapsed : "))
    n = float(input("Enter the number of times interest applied per time period : "))    
    CI = compoundInterest(p,r,n,t)
    print("The Compound Interest is ₹ {:.2f}".format(CI))
    