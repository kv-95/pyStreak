# Python Program to check Armstrong Number

def isArmstrong(number):
    sum = 0
    for n in number:
        sum += int(n)**3
    if sum == int(number):
        print("It is an Armstrong Number")
    else:
        print("It is not an Armstrong Number")
        
if __name__ == "__main__":
    number = input("Enter a 3 digit number: ")  
    isArmstrong(number)
    