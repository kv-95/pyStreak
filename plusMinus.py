
def plusMinus(arr):
    c1 = 0
    c2 = 0
    c3 = 0
    for i in arr:
        if i > 0 :
            c1 +=1
        elif i < 0 :
            c2+= 1
        elif  i== 0 :
            c3+=1
            
      
    print("%1.6f "%(c1/len(arr))) 
    print("%1.6f "%(c2/len(arr)))  
    print("%1.6f "%(c3/len(arr)))  
    # Write your code here

if __name__=='__main__':
   
    n= int(input("Enter the number of elements in array:"))
    arr=[]
    for i in range(n):
        num=int(input("Enter the elements in array:"))
        arr.append(num)
    plusMinus(arr)