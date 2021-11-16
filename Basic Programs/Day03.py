# Python Program for simple interest

def simpleInterest(p,r,t):
    return (p*r*t)/100
if __name__ == "__main__":
    p = float(input("Enter the Principal Amount (₹): "))
    r = float(input("Enter the Rate of Interest in Percentage : "))
    t = float(input("Enter the Time period : "))
    SI = simpleInterest(p, r, t)
    print("The Simple Interest is ₹",SI,sep="")