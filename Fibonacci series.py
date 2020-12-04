#Fibonacci series

first=0
second=1
n=int(input("Enter the number of terms"))
if(n<=0):
    print("The series is ",first)
else:
    print("The series is ",first,"",second,"",end="")
for i in range(2,n):
    next=first+second 
    print(next,"",end="")
    first=second
    second=next
    
