#Maximum of three numbers

def findMax(num1,num2,num3):
    if num1>num2 & num1>num3:
        max = num1
    elif num2>num1 & num2>num3:
        max = num2
    else:
        max = num3
    return max
 
if __name__ == "__main__":
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    num3 = int(input("Enter the third number : "))
    maximum = findMax(num1, num2, num3)
    print("The highest among the three numbers is", maximum)