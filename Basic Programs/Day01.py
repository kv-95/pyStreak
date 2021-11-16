# Largest of three numbers

def findMax(num1,num2,num3):
    if num1>num2 & num1>num3:
        return num1
    elif num2>num1 & num2>num3:
        return num2
    else:
        return num3
 
if __name__ == "__main__":
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    num3 = int(input("Enter the third number : "))
    maximum = findMax(num1, num2, num3)
    print("The highest among the three numbers is", maximum)