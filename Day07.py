# Python program to print all Prime numbers in an Interval
def Prime(interval):
    prime = [] 
    for i in range(int(interval[0]),int(interval[1])+1):
        flag = 0
        for j in range(2,i):
            if i % j  == 0:
                flag = 1
                break
        if flag == 0:
            prime.append(i)
        
    return prime

if __name__== '__main__':
    interval =input("Enter the lower and upper limit separated by space:").split(" ")
    print("The prime numbers between the interval({:d},{:d}) are".format(int(interval[0]),int(interval[1])), Prime(interval))
     